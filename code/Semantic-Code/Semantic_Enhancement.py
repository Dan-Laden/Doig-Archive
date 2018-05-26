#################################
# author@ Daniel Laden          #
# email@ dthomasladen@gmail.com #
#################################

print("Test File")#This is only a test files this shouldn't be used for production
import time
start_time = time.time()

import nltk #ref doc: http://www.nltk.org/howto/index.html
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import words
from nltk  import FreqDist
import string #ref doc: https://docs.python.org/3.3/library/string.html?highlight=string#module-string
import re #ref doc: https://docs.python.org/3/library/re.html#re.ASCII
import PyPDF2 #ref doc: https://pythonhosted.org/PyPDF2/
import difflib #Library that can compare differences in strings ref doc: https://docs.python.org/3.3/library/difflib.html?highlight=difflib#module-difflib
import multiprocessing #ref doc: https://docs.python.org/3.6/library/multiprocessing.html
import sys #ref doc: https://docs.python.org/3.6/library/sys.html
import os #ref doc: https://docs.python.org/3.6/library/os.html
import sqlite3 #ref doc: https://docs.python.org/3/library/sqlite3.html
import errno #ref doc: https://docs.python.org/3.6/library/errno.html
from geopy.geocoders import GeoNames #ref doc: http://geopy.readthedocs.io/en/stable/#

stoplist = set(stopwords.words('english'))#set of all stopwords in english thanks to nltk

#########################
#Main functions for data parsing

#Main function that executes all the functions before for parsing, dividing, and serving up enriched text.
def semanticActions(key, text, pages, source, queue):
    tokens = POStagging(text)
    keywords = keywordGenerator(tokens)
    places = multiwordPlace(tokens)
    geoplaces = geoServer(places)
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
def keywordGenerator(POStext):
    keywordsNN = []
    keywordsVB = []
    keywordsNN2chr = [] #For testing and debate on weither or not to include 2 character strings as nouns
    for token in POStext:
        noun = re.compile('NN(\S*)')#Looks for any POS labeled NN* NN with any variation on it
        verb = re.compile('VB(\S*)')#Looks for any POS labled VB* VB with any variation on it
        doig = re.compile('(\S*)Doig(\S*)')
        if noun.match(token[1]):
            if(len(token[0])<3):
                keywordsNN2chr.append(token[0])
            else:
                if not(doig.match(token[0])):
                    keywordsNN.append(token[0])
        elif verb.match(token[1]):
            if not(doig.match(token[0])):
                keywordsVB.append(token[0])
    return (keywordsNN, keywordsVB)

#This function outputs two text files of rich text for additional sourcing
def output(filename, rawtext, keylist, geolocations, pages, source, queue):
    #write general text to a .txt file
    filetypes = ["Raw", "Keywords", "Geolocations"]

    img = filename+".png"

    keywordlist = ""
    for keywords in keylist:
        for key in keywords:
            keywordlist = keywordlist + key + "; "
    geolocation = ""
    for geoloc in geolocations:
        geolocation = geolocation + geoloc.address + "; "


    for types in filetypes:
        path = "output/"+filename[:(len(filename))-2]+"/"+types+"/"+types+"-"+filename+".txt"
        makedir(path)
        f = open(path, "w")

        if(types == "Raw"):
            f.write(rawtext)
        elif(types == "Keywords"):
            f.write(keywordlist)
        else:
            f.write(geolocation)

        f.close()


        
    filename = filename.replace("-", " ")
    digits = re.findall('\d+', filename)
    digit = digits[0]
    source = filename.replace((" "+digit), "")
    filename = filename.replace((" "+digit), (", Chapter "+digit))



    queue.put(Item(filename, rawtext, keywordlist, pages, source, geolocation, img))
    print("Output for "+filename+" finished")

def fillItemDB(item):
    connection = sqlite3.connect("items.db")
    cursor = connection.cursor()

    sql_addto = """INSERT INTO ITEMS (ID, RawText, Keyword, Pages, RelatedBook, Geolocation, Img)
    VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}');""".format(item.ID, item.rawText, item.keywords, item.pages, item.relatedBook, item.geolocations, item.img)
    cursor.execute(sql_addto)

    # necessary for saving changes made
    connection.commit()

    connection.close()

def clearItemDB():
    connection = sqlite3.connect("items.db")
    cursor = connection.cursor()

    try:
        #For cleaning the database for testing
        cursor.execute("""DELETE FROM ITEMS;""")

        # necessary for saving changes made
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
        PRIMARY KEY(ID)
        );"""
        cursor.execute(sql_createtb)

    connection.commit()

    connection.close()


class Item:#For database usage
    def __init__(self, inID, inRawText, inKeywords, inPages, inRelatedBook, inGeolocations, inImg):
        self.ID = inID
        self.rawText = inRawText
        self.keywords = inKeywords
        self.pages = inPages
        self.relatedBook = inRelatedBook
        self.geolocations = inGeolocations
        self.img = inImg

#This function creates a list of compound places to iterate through for locational checking.
#Creates two or more string tokens
def multiwordPlace(POStext):
    compoundLoc = []
    index = 0
    while index < len(POStext):
        try:
            if POStext[index][1] == 'NNP' and POStext[index+1][1] == 'NNP':
                    POStext[index] = (POStext[index][0] + " " + POStext[index+1][0], 'NNP')
                    compoundLoc.append(POStext[index])
                    #del POStext[index+1]
            index+=1
        except IndexError:
            index+=1
            #do nothing

    return compoundLoc

class Geothing:#For testing
    def __init__(self):
        self.address = "placeholder"

#This function takes in a list of places and tries it's best to locate what is possibly a match

def geoServer(listPlaces):
    #Using Geopy for geolocations
    GeoNamesAccounts = ["semantic_1", "semantic_2", "semantic_3", "semantic_4", "semantic_5", "semantic_6"]
    geolocator = GeoNames(username="dan_laden")
    geolocations = []
    process_queue = []
    global numOfPlaces
    numOfPlaces = 0
    queue = multiprocessing.Queue()
    for loc in listPlaces: #TODO next change with a list of accounts to login with
        #p = multiprocessing.Process(target=geoLocate, args=(loc[0], queue, geolocator))
        #p.start()
        #process_queue.append(p)
        geolocations.append(Geothing())#For now this has a placeholder class till XXX usage of this API is resolved

    #makes sure all the processes started above are killed before finishing the program.
    time.sleep(30)
    while numOfPlaces > 0:#wait
        if queue.empty():
            print("Nothing in queue")
            time.sleep(0.1)
        else:
            geolocations.append(queue.get())
            numOfPlaces-=1

    for proc in process_queue:
        proc.terminate()

    return geolocations

#This takes a list and converts is into a string
#This function goes along with stripNonAlphaNumASCII since it returns a list normally
def listToString(list):
    returnStr = ''
    for STR in list:
        returnStr = returnStr +" "+ STR
    return returnStr


#This function is used by a multiprocessing queue in geoServer. This is where all locations are resolved
def geoLocate(location, queue, geoloc):
    geo = geoloc.geocode(location, timeout=20)
    if not geo == None:
        if not "MT" in geo.address:
            locMT = location+ " MT"
            geo = geoloc.geocode(locMT, timeout=20)
        if not geo == None and "MT" in geo.address:
            queue.put(geo)
            numOfPlaces+=1


#NOTE: not my code this is from: https://stackoverflow.com/a/12517490/8967976
#This is to create the directories for the files being outputted
def makedir(path):
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
#End of functions for data parsing
#########################

#########################
# NOTE Start of main code
numOfFiles = 0
rawFiles = {}
argc = 1 #for all the directories to go into
if(argc == len(sys.argv)):#If this program gets no directories to use it immediately exits
    print("Please include files to parse")
    exit()
while(argc<len(sys.argv)):#Opening the file and putting it through the PDF reader.
    count = 1 #Due to naming conventions all chapters of books will be source/[bookname]/[bookname]-[chapter number]
    filepath = "source/"+sys.argv[argc]#NOTE: you should enter the directory you have the files you want to parse inside
    if(os.path.exists(filepath)):      #      the directory should contained numbered pdf files with the same name as the directory
        key = sys.argv[argc]+"-"+(str)(count)
        path = filepath+"/"+key+".pdf"
        while(os.path.exists(path)):
            f = open(path, 'rb')
            pdf = PyPDF2.PdfFileReader(f)
            pages = pdf.getNumPages()
            rawText = readText(pdf)
            rawFiles[key] = (rawText, pages, sys.argv[argc]) #Reads in the text then puts it in a dictionary with a lable of the filename.
            count+=1
            numOfFiles+=1
            key = sys.argv[argc]+"-"+(str)(count)
            path = filepath+"/"+key+".pdf"

    #If the folder holding the chapters isn't found this prints out then continues running through.
    elif(not(os.path.exists(filepath)) and filepath == ("source/"+sys.argv[argc])):
        print(sys.argv[argc]+" is not a valid directory please try again next run")

    argc+=1

print("--- %s loading files time seconds ---" % (time.time() - start_time))


process_queue = []
itemQueue = multiprocessing.Queue()
for key in rawFiles: #performs all the semantic actions in sequence
    p = multiprocessing.Process(target=semanticActions, args=(key, rawFiles[key][0],rawFiles[key][1], rawFiles[key][2], itemQueue,  ))
    p.start()
    process_queue.append(p)


#while loop the queue size till it equals how many parsed in files? no using .join() just wait till all information gets moved into the Queue then
#terminated all threads
print("--- %s seconds to parse all files---" % (time.time() - start_time))


time.sleep(30)

clearItemDB()
while numOfFiles > 0:#wait
    if itemQueue.empty():
        print("Nothing in queue")
        time.sleep(0.1)
    else:
        print("Filling DB")
        fillItemDB(itemQueue.get())
        numOfFiles-=1



#makes sure all the processes started above are killed before finishing the program.
for proc in process_queue:
    print("terminate loop")
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
#########################
