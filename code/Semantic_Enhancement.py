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
import multiprocessing
import sys
import os
import errno
from geopy.geocoders import GeoNames #ref doc: http://geopy.readthedocs.io/en/stable/#

stoplist = set(stopwords.words('english'))#set of all stopwords in english thanks to nltk

#########################
#Main functions for data parsing

def semanticActions(dictionary):
    for key in dictionary:
        tokens = POStagging(dictionary[key])
        keywords = keywordGenerator(tokens)
        places = multiwordPlace(tokens)
        geoplaces = geoServer(places)
        output(key, dictionary[key], keywords, geoplaces)

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
    keywordsNN2chr = []
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
def output(filename, rawtext, keywordlist, geolocations):
    #write general text to a .txt file
    path = "output/Raw/Raw-"+filename+".txt"
    makedir(path)
    f = open(path, "w")

    f.write(rawtext)

    f.close()

    #write keywords to a .txt file

    path = "output/Keywords/"+filename+"-Keywords.txt"
    makedir(path)
    f = open(path, "w")
    for keywords in keywordlist:
        for key in keywords:
            f.write(key+"; ")

    f.close()

    #write geolocations to a .txt file
    path = "output/Geolocations/"+filename+"-Geolocations.txt"
    makedir(path)
    f = open(path, "w")

    for geoloc in geolocations:
        f.write(geoloc.address+"; ")

    f.close()

#This function creates a list of compound places to iterate through for locational checking.
def multiwordPlace(POStext):
    compoundLoc = []
    index = 0
    while index < len(POStext):
        if POStext[index][1] == 'NNP' and POStext[index+1][1] == 'NNP':
            POStext[index] = (POStext[index][0] + " " + POStext[index+1][0], 'NNP')
            compoundLoc.append(POStext[index])
            #del POStext[index+1]
        index+=1
    return compoundLoc

#This function takes in a list of places and tries it's best to locate what is possibly a match
def geoServer(listPlaces):
    #Using Geopy for geolocations
    geolocator = GeoNames(username="dan_laden")
    geolocations = []
    queue = multiprocessing.Queue()
    for loc in listPlaces:
        p = multiprocessing.Process(target=geoLocate, args=(loc[0], queue, geolocator))
        p.start()

    time.sleep(30)#Wait till everything finishes

    while not queue.empty():
        geolocations.append(queue.get_nowait())
    return geolocations

#This takes a list and converts is into a string
#This function goes along with stripNonAlphaNumASCII since it returns a list normally
def listToString(list):
    returnStr = ''
    for STR in list:
        returnStr = returnStr +" "+ STR
    return returnStr

#TODO: Optional idea but make it so Diff doesn't print the lines that don't change.
#This will check the difference between the two lists
def checkDiff(list1, list2):
    d = difflib.Differ()
    diff = d.compare(list1, list2)
    print ('\n'.join(diff))

def createFreqDist(keyword):
    return FreqDist(keyword)

def geoLocate(location, queue, geoloc):
    geo = geoloc.geocode(location, timeout=20)
    if not geo == None:
        if not "MT" in geo.address:
            locMT = location+ " MT"
            geo = geoloc.geocode(locMT, timeout=20)
        if not geo == None and "MT" in geo.address:
            queue.put(geo)


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
rawFiles = {}
argc = 1 #for all the directories to go into
if(argc == len(sys.argv)):
    print("Please include files to parse")
    exit()
while(argc<len(sys.argv)):#Opening the file and putting it through the PDF reader.
    count = 1 #Due to naming conventions all chapters of books will be source/[bookname]/[bookname]-[chapter number]
    filepath = "source/"+sys.argv[argc]#NOTE:
    if(os.path.exists(filepath)):
        key = sys.argv[argc]+"-"+(str)(count)
        path = filepath+"/"+key+".pdf"
        while(os.path.exists(path)):
            f = open(path, 'rb')
            rawText = readText(PyPDF2.PdfFileReader(f))
            rawFiles[key] = rawText
            count+=1
            key = sys.argv[argc]+"-"+(str)(count)
            path = filepath+"/"+key+".pdf"

    #If the folder holding the chapters isn't found this prints out then continues running through.
    elif(not(os.path.exists(filepath)) and filepath == ("source/"+sys.argv[argc])):
        print(sys.argv[argc]+" is not a valid directory please try again next run")

    argc+=1

semanticActions(rawFiles)

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
#########################
