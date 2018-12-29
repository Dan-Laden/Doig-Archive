#################################
# author@ Daniel Laden          #
# email@ dthomasladen@gmail.com #
#################################
#Test
print("Main File")
import time
start_time = time.time()

import nltk #ref doc: http://www.nltk.org/howto/index.html
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import words
from nltk import FreqDist
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import string #ref doc: https://docs.python.org/3.3/library/string.html?highlight=string#module-string
import re #ref doc: https://docs.python.org/3/library/re.html#re.ASCII
import PyPDF2 #ref doc: https://pythonhosted.org/PyPDF2/
import difflib #Library that can compare differences in strings ref doc: https://docs.python.org/3.3/library/difflib.html?highlight=difflib#module-difflib
import multiprocessing #ref doc: https://docs.python.org/3.6/library/multiprocessing.html
import sys #ref doc: https://docs.python.org/3.6/library/sys.html
import os #ref doc: https://docs.python.org/3.6/library/os.html
import sqlite3 #ref doc: https://docs.python.org/3/library/sqlite3.html
import errno #ref doc: https://docs.python.org/3.6/library/errno.html
import operator #ref doc: https://docs.python.org/3/library/operator.html
import random
from geopy.geocoders import GeoNames #ref doc: http://geopy.readthedocs.io/en/stable/#

stoplist = set(stopwords.words('english'))#set of all stopwords in english thanks to nltk

#########################
#Global variables
global numOfPlaces
global PROCESS_LIMIT
global MINIMAL_VERB
global MINIMAL_NOUN

PROCESS_LIMIT = 30
MINIMAL_VERB = 10
MINIMAL_NOUN = 5

#End of Global variables
#########################

#########################
#Main classes for relation building

#This is the python object that holds everything for a database entry
class Item:#For database usage
    def __init__(self, inID, inRawText, inKeywords, inPages, inRelatedBook, inGeolocations, inImg, inEmotion):
        self.ID = inID
        self.rawText = inRawText
        self.keywords = inKeywords
        self.pages = inPages
        self.relatedBook = inRelatedBook
        self.geolocations = inGeolocations
        self.img = inImg
        self.emotion = inEmotion
#End of class for semantic enhancement
#########################


#########################
#Main functions for data parsing

#Main function that executes all the functions before for parsing, dividing, and serving up enriched text.
def semanticActions(key, text, pages, source, locations, queue):
    tokens = POStagging(text)
    keywords = keywordGenerator(tokens, source)
    places = multiwordPlace(tokens)
    geoplaces = geoLocate(places, locations)
    output(key, text, keywords, geoplaces, pages, source, queue)

#This function reads in text from a pdf and returns it without punctuation
def readText(pdfR):
    #Grabbing all the text from the PDF
    text = ""
    for i in range(0, pdfR.getNumPages()):
    #    print("==========================\n=\tPage "+(str)(i+1)+"\n==========================")
        page = pdfR.getPage(i)
        text = text + page.extractText()
    #    print(page.extractText())
    f.close()

    #Removing all the punctuation from the text.
    translate_table = dict((ord(char), None) for char in string.punctuation)
    return stripNonAlphaNumASCII(text.translate(translate_table))

#This function removes strange characters that are read in by the PDF reader
def stripNonAlphaNumASCII(text):
    return listToString(re.compile(r'\W+', re.ASCII).split(text))

#This function returns a list of all Part of Speech tags in the put in text
def POStagging(text):
    #Using this to remove random non-ASCII characters that are from the PDF reader
    tokenized_set = word_tokenize(text)
    tokenized_set_nostop = [token for token in tokenized_set if token not in stoplist]

    #putting POS on the list of tokens without stopwords and non-ASCII characters
    return nltk.pos_tag(tokenized_set_nostop)

#This function returns two different types of keywords (nouns, verbs)
def keywordGenerator(POStext, source):
    keywordsNN = []
    keywordsVB = []
    keywordsNN2chr = [] #For testing and debate on weither or not to include 2 character strings as nouns
    ps = PorterStemmer() #This checks verb forms to make sure it's the root instead of anything 'ing' 's' 'es' or additional verb fluff
    for token in POStext:
        noun = re.compile('NN(\S*)')#Looks for any POS labeled NN* NN with any variation on it
        verb = re.compile('VB(\S*)')#Looks for any POS labled VB* VB with any variation on it
        doig = re.compile('(\S*)Doig(\S*)')
        if noun.match(token[1]):
            if(len(token[0])<3):
                keywordsNN2chr.append(token[0])
            else:
                if source == "Sweet-Thunder":
                    if token[0] == "Thunder" or token[0] == "Sweet" or token[0] == "Deleted":
                        continue
                if token[0].isupper(): #This should remove chapter names and read in errors that have no application to the chapter at all
                    continue
                if not(doig.match(token[0])):
                    keywordsNN.append(token[0])
        elif verb.match(token[1]):
            if not(doig.match(token[0])):
                verb = ps.stem(token[0]) #get the stem of the verb
                keywordsVB.append(verb)


    keywordsNN = KeywordCounter(keywordsNN)
    keywordsVB = KeywordCounter(keywordsVB)

    #All forloops here are for removing nouns and verbs that don't fall into the threshold values
    keywordsNNremove = []
    keywordsVBremove = []#first two loops are for gathering what to remove
    for keyword in keywordsNN:
        if keyword[1] < MINIMAL_NOUN and not keyword[0].istitle():#isupper() is needed so we don't remove proper nouns since common nouns have less value
            keywordsNNremove.append(keyword)

    for keyword in keywordsVB:
        if keyword[1] < MINIMAL_VERB:
            keywordsVBremove.append(keyword)

    #last two loops are for removing from the main keyword lists
    for keyword in keywordsNNremove:
        keywordsNN.remove(keyword)

    for keyword in keywordsVBremove:
        keywordsVB.remove(keyword)
                                   #DONE
    return (keywordsNN, keywordsVB)#TODO Output this differently to fix nouns and verbs

#This creates a frequency dictionary for the number of occurences in the keywordList and returns them ordered by number of occurences
def KeywordCounter(keywordList):
    freq = FreqDist(keywordList)
    sorted_freq = sorted(freq.items(), key=operator.itemgetter(1))
    sorted_freq.reverse()
    return sorted_freq


#This function outputs two text files of rich text for additional sourcing
def output(filename, rawtext, keylist, geolocations, pages, source, queue):
    #write general text to a .txt file
    filetypes = ["Raw", "Keywords", "Geolocations"]

    sentiment = getSentiment(rawtext)

    keywordlist_text = ""
    keywordlist_db = ""
    for keywords in keylist:
        for key in keywords:
            keywordlist_db = keywordlist_db + key[0] +"; "
            keywordlist_text = keywordlist_text + key[0] + "|" + (str)(key[1]) + "; "

    keywordlist_text = keywordlist_text + sentiment + "|" + "SENTIMENT"+"; "
    geolocation = ""
    throw_aways = re.compile('((M|m)arker|(H|h)istor[a-zA-Z]*)')#Historical Markers are getting picked up and to my knowledge I don't think they're anything relevent to the project
    for geoloc in geolocations:
        if "(" in geoloc[0] or "'" in geoloc[0] or throw_aways.match(geoloc[0]):
            continue
        elif "Gros Ventre" in geoloc[0]:
            geoloc = list(geoloc)
            geoloc[0] = "Gros Ventre, MT, US"
        geolocation = geolocation + geoloc[0] + "|" + (str)(geoloc[1]) + "; "

    #outputs rawtext, keywords, and geolocations to text files
    for types in filetypes:
        #NOTE If larger books are inserted this might need to be changed if chapters go over 3 digits and so on to catch all cases
        try: #some-file-14   len(filename) will get "-14" which is a negative number if it's some-file-1 it will get "e-1" which isn't a number
            value = (int)(filename[(len(filename))-3:])
            path = "output/"+filename[:(len(filename))-3]+"/"+types+"/"+types+"-"+filename+".txt"
        except ValueError:
            value = (int)(filename[(len(filename))-2:])
            path = "output/"+filename[:(len(filename))-2]+"/"+types+"/"+types+"-"+filename+".txt"
        makedir(path)
        f = open(path, "w")

        if(types == "Raw"):
            f.write(rawtext)
        elif(types == "Keywords"):
            f.write(keywordlist_text)
        else:
            f.write(geolocation)

        f.close()

    #This creates the "Proper" file names to be used in the dynamic pages
    #filename is the title of the book while source is the related book
    filename = filenameFix(filename)
    img = "img/"+source+"/"+(str)(value)+".png"
    img = img.replace((" "), "-")


    #puts the database item in a queue to be pulled later
    queue.put(Item(filename, rawtext, keywordlist_db, pages, source, geolocation, img, sentiment))
    print("Output for "+filename+" finished")

#This method fills the database with a new item from the itemQueue
def fillItemDB(item):
    connection = sqlite3.connect("items.db")
    cursor = connection.cursor()

    sql_addto = """INSERT INTO ITEMS (ID, RawText, Keyword, Pages, RelatedBook, Geolocation, Img, Emotion)
    VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}');""".format(item.ID, item.rawText, item.keywords, item.pages, item.relatedBook, item.geolocations, item.img, item.emotion)

    try:
        cursor.execute(sql_addto)

        # necessary for saving changes made
        connection.commit()

    except:
        print("ERROR: "+item.ID+" already exists in item.db")

    connection.close()

#This method cleans the database from previous uses
def clearItemDB():
    connection = sqlite3.connect("items.db")
    cursor = connection.cursor()

    #For cleaning the database for testing
    try:

        cursor.execute("""DELETE FROM ITEMS;""")
        print("Database clear")


    #This  is for if the database is new and a table for the items is needed to be created.
    except sqlite3.OperationalError:
        print("Detect no previous database, one will be made.")

        sql_createtb = """CREATE TABLE `ITEMS` (
        `ID`	TEXT,
        `RawText`	TEXT,
        `Keyword`	TEXT,
        `Pages`	INTEGER,
        `RelatedBook`	TEXT,
        `Geolocation`	TEXT,
        `Img`	TEXT,
        'Emotion'   TEXT,
        PRIMARY KEY(ID)
        );"""
        cursor.execute(sql_createtb)

    # necessary for saving changes made
    connection.commit()


    connection.close()


#This function creates a list of compound places to iterate through for locational checking.
#Creates two or more string tokens
def multiwordPlace(POStext):
    compoundLoc = []
    potentialLoc = []
    index = 0
    while index < len(POStext):
        try:
            if POStext[index][1] == 'NNP':
                if POStext[index+1][1] == 'NNP':
                    compound = (POStext[index][0] + " " + POStext[index+1][0], 'NNP')
                    compoundLoc.append(compound)
                else:
                    potentialLoc.append(POStext[index])
            index+=1
        except IndexError:
            index+=1
            #do nothing

    return compoundLoc + potentialLoc

# #This function takes in a list of places and tries it's best to locate what is possibly a match
# def geoServer(listPlaces): #TODO #TODO #TODO
#     #Using Geopy for geolocations
#     GeoNamesAccounts = ["semantic_1", "semantic_2", "semantic_3", "semantic_4", "semantic_5", "semantic_6", "semantic_7", "semantic_8", "semantic_9", "semantic_10", "semantic_11", "semantic_12"]
#     geolocator = GeoNames(username="dan_laden")
#     geolocations = []
#     process_queue = []
#     numOfPlaces = 0 #keeps track of how many places are caught by the geolocator for the queue extraction
#     queue = multiprocessing.Queue()
#     for loc in listPlaces: #TODO next change with a list of accounts to login with
#         #p = multiprocessing.Process(target=geoLocate, args=(loc[0], queue, geolocator))
#         #p.start()
#         #process_queue.append(p)
#         geolocations.append(Geothing())#For now this has a placeholder class till XXX usage of this API is resolved
#
#     #makes sure all the processes started above are killed before finishing the program.
#     time.sleep(30)
#     while numOfPlaces > 0:#wait
#         if queue.empty():
#             print("Nothing in queue")
#             time.sleep(0.1)
#         else:
#             geolocations.append(queue.get())
#             numOfPlaces-=1
#
#     for proc in process_queue:
#         proc.terminate()
#
#     return geolocations

#This takes a list and converts is into a string
#This function goes along with stripNonAlphaNumASCII since it returns a list normally
def listToString(list):
    returnStr = ''
    for STR in list:
        returnStr = returnStr +" "+ STR
    return returnStr


#This function is used by a multiprocessing queue in geoServer. This is where all locations are resolved
def geoLocate(list_of_places, list_of_locations):
    #Using Geopy for geolocations NOTE this works
    GeoNamesAccounts = ["semantic_1", "semantic_2", "semantic_3", "semantic_4", "semantic_5", "semantic_6"]
    holder = []
    holder = holder + GeoNamesAccounts
    counter = 1
    geolocations = []
    choice = random.choice(GeoNamesAccounts)
    GeoNamesAccounts.remove(choice)
    geolocator = GeoNames(username=choice)


    #removing duplicates to be sure it should already be distinct 
    places = list(set(list_of_places))

    for place in places:
        if counter >= 1500:
            try:
                choice = random.choice(GeoNamesAccounts)
            except:
                GeoNamesAccounts = holder + GeoNamesAccounts
                choice = random.choice(GeoNamesAccounts)
            GeoNamesAccounts.remove(choice)
            geolocator = GeoNames(username=choice)
            counter = 1

        try:
            geo = geolocator.geocode(place[0], timeout=10)
            index = 0
            while geo != None:
                for location in list_of_locations:
                    if not location in geo.address:
                        continue
                    if location in geo.address:
                        geolocations.append(geo)
                        break

                if index >= len(list_of_locations):
                    break
                else:
                    new_place = place[0] + list_of_locations[index]
                    index+=1
                    try:
                        geo = geolocator.geocode(new_place, timeout=10)
                    except:
                        pass
        except:
            continue



            #append location onto place and recheck if it comes up with anything before timeout
        counter += 1

    geoplaces = []
    for geoloc in geolocations:
        geoplaces.append(geoloc.address)

    geolocations = KeywordCounter(geoplaces)
    return geolocations


#NOTE: not my code this is from: https://stackoverflow.com/a/12517490/8967976
#This is to create the directories for the files being outputted
def makedir(path):
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def filenameFix(filename):
    filename = filename.replace("-", " ")
    digits = re.findall('\d+', filename)#I'm using regular expressions instead of forloops because I think that's faster proformance
    digit = digits[0]
    source = filename.replace((" "+digit), "")
    filename = filename.replace((" "+digit), (", Chapter "+digit))
    return filename

#This function returns the sentiment values for the entered in text
def getSentiment(entered_text):
    f=open("NRC-Emotion-Lexicon-Wordlevel-v0.92.txt", 'r')
    active_word = " "
    emotion_dictionary = {}
    for line in f:
        words = line.split()
        empty_dict = {}
        if words[0] != active_word:
            active_word = words[0]
            emotion_dictionary[words[0]] = empty_dict

        emotion_dictionary[words[0]][words[1]] = (int)(words[2])

    entered_text = entered_text.split()

    f.close()

    positivity_rating = 0
    emotions = {"fear" : 0,  "anger" : 0, "sadness" : 0, "joy" : 0, "disgust" : 0, "surprise" : 0, "trust" : 0, "anticipation" : 0}
    for word in entered_text:
        if word in emotion_dictionary:
            #print(word + " : " + (str)(emotion_dictionary[word]))
            for emotion in emotions:
                emotions[emotion] = emotions[emotion] + emotion_dictionary[word][emotion]

            positivity_rating = positivity_rating + emotion_dictionary[word]["positive"] - emotion_dictionary[word]["negative"]


    top_emotion = "trust"
    for emotion in emotions: #TODO TODO TODO just kinda toy with this and see what other emotions I can get out of the output
                             #Email Milman about this and ask what he thinks of this constant trust/anticipation output. maybe provide
                             #ideas about better emotional output
        if(emotions[top_emotion]<emotions[emotion] and emotion != "trust" and emotion != "anticipation"):
            top_emotion = emotion


    if(positivity_rating>0):
        tone = "positive"
    elif(positivity_rating<0):
        tone = "negative"
    else:
        tone = "neutral"

    if(top_emotion == "trust"):
        top_emotion = "apathetic"

    textural_emotion = tone + " " + top_emotion

    return textural_emotion


#End of functions for data parsing
#########################

#########################
# NOTE Start of main code
numOfFiles = 0 #keeps track of how many files have been loaded in the program
nameOfFiles = []
rawFiles = {}
argc = 2 #for all the directories to go into
if((sys.argv[1] != "--new" and sys.argv[1] != "--old")  or argc > len(sys.argv)):
    print("========Semantic_Enhancement.py========\n\n"+
          "This program runs by using python3, and example input that is valid follows\n"+
          "python3 Semantic_Enhancement.py --new example_folder_1 example_folder_2\n\n"+
          "Run Options:\n\n"+
          "--new\n"+
          "For first time runs, this will create a database for the program to store data the program will also clear "+
          "a database if one exists already giving it a fresh new state.\n\n"+
          "--old\n"+
          "For runs after creating a database, this is for adding to a database without erasing old data. "+
          "Any new folders to parse should run using this command.\n\n"+
          "========Semantic_Enhancement.py========\n")
    exit()
elif(argc == len(sys.argv)):#If this program gets no directories to use it immediately exits
    print("Please include files to parse")
    exit()

while(argc<len(sys.argv)):#Opening the file and putting it through the PDF reader.
    locations = []
    count = 1 #Due to naming conventions all chapters of books will be source/[bookname]/[bookname]-[chapter number]
    filepath = "source/"+sys.argv[argc]#NOTE: you should enter the directory you have the files you want to parse inside
    if(os.path.exists(filepath)):      #the directory should contained numbered pdf files with the same name as the directory
        key = sys.argv[argc]+"-"+(str)(count)
        rawName = sys.argv[argc]
        nameOfFiles.append(key)
        path = filepath+"/"+key+".pdf"
        argc+=1
        while(os.path.exists(path)):
            f = open(path, 'rb')#trying to use location as part of the filesystem
            pdf = PyPDF2.PdfFileReader(f)
            pages = pdf.getNumPages()
            rawText = readText(pdf)
            while argc<len(sys.argv) and "-" not in sys.argv[argc]:
                locations.append(sys.argv[argc].replace(("_"), " "))
                argc+=1

            rawFiles[key] = (rawText, pages, rawName, locations) #Reads in the text then puts it in a dictionary with a lable of the filename.
            count+=1
            numOfFiles+=1
            key = rawName+"-"+(str)(count)
            path = filepath+"/"+key+".pdf"

    #If the folder holding the chapters isn't found this prints out then continues running through.
    elif(not(os.path.exists(filepath)) and filepath == ("source/"+sys.argv[argc])):
        print(sys.argv[argc]+" is not a valid directory please try again next run")
        argc+=1



print("--- %s loading files time seconds ---" % (time.time() - start_time))


process_queue = []
itemQueue = multiprocessing.Queue()
if(sys.argv[1] == "--new"):
    clearItemDB()
activeProcesses = 0
for key in rawFiles: #performs all the semantic actions in sequence
    p = multiprocessing.Process(target=semanticActions, args=(key, rawFiles[key][0],rawFiles[key][1], rawFiles[key][2], rawFiles[key][3], itemQueue,  ))
    p.start()
    process_queue.append(p)
    if activeProcesses > PROCESS_LIMIT: #stops the program from creating more processes and killing the system
        print("Halting processing time halted %s" % (time.time() - start_time))
        while activeProcesses != 0:
            if itemQueue.empty():
                #print("Nothing in queue")
                time.sleep(0.1)
            else:
                #print("Filling DB")
                item = itemQueue.get()
                fillItemDB(item)
                numOfFiles-=1
                activeProcesses-=1
    else:
        activeProcesses+=1



#While the program waits for the last files to be processes it will wait in the while and keep taking short sleeps until a file is detected in the itemQueue
while numOfFiles > 0:#wait
    if itemQueue.empty():
        #print("Nothing in queue")
        time.sleep(0.1)
    else:
        #print("Filling DB")
        item = itemQueue.get()
        fillItemDB(item)
        numOfFiles-=1

#makes sure all the processes started above are killed before finishing the program.
for proc in process_queue:
    #print("terminate loop")
    proc.terminate()
print("--- %s seconds to load all information in the databases ---" % (time.time() - start_time))
#End of main code
#########################

print("--- %s seconds ---" % (time.time() - start_time))
#########################
#resources used for code so far
#
# https://stackoverflow.com/questions/15547409/how-to-get-rid-of-punctuation-using-nltk-tokenizer
# https://github.com/nltk/nltk/wiki/Frequently-Asked-Questions-(Stackoverflow-Edition)
# https://programminghistorian.org/lessons/normalizing-data
# https://pymotw.com/2/difflib/
# https://www.guru99.com/python-regular-expressions-complete-tutorial.html
# https://stackoverflow.com/questions/156360/get-all-items-from-thread-queue
# https://stackoverflow.com/questions/39773377/python-multiprocessing-check-status-of-each-processes
# https://stackoverflow.com/questions/34584629/regex-for-catching-only-upper-case-matches/34584693
# https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output
# https://stackoverflow.com/questions/1559125/string-arguments-in-python-multiprocessing #XXX stupidest error yet
# https://stackoverflow.com/questions/33152171/why-does-multiprocessing-process-join-hang #XXX this was related to the multiprocessing .join() errors.
# https://stackoverflow.com/questions/4289331/python-extract-numbers-from-a-string
# https://www.tutorialspoint.com/python/string_replace.htm
# https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists
# https://stackoverflow.com/questions/7353968/checking-if-first-letter-of-string-is-in-uppercase/7354011
# https://pythonspot.com/nltk-stemming/ for the PorterStemmer
#########################
