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
from geopy.geocoders import GeoNames #ref doc: http://geopy.readthedocs.io/en/stable/#

stoplist = set(stopwords.words('english'))#set of all stopwords in english thanks to nltk

#########################
#Main functions for data parsing

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
    return text.translate(translate_table)

#This function removes strange characters that are read in by the PDF reader
def stripNonAlphaNumASCII(text):
    return listToString(re.compile(r'\W+', re.ASCII).split(text))

#This function returns a list of all Part of Speech tags in the put in text
def POStagging(text):
    #Using this to remove random non-ASCII characters that are from the PDF reader
    textASC = stripNonAlphaNumASCII(text)
    tokenized_set_ASCII = word_tokenize(textASC)
    tokenized_set_nostop_ASCII = [token for token in tokenized_set_ASCII if token not in stoplist]

    #putting POS on the list of tokens without stopwords and non-ASCII characters
    return nltk.pos_tag(tokenized_set_nostop_ASCII)

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
def output(filename, rawtext, keywords):
    #write general text to a .txt file
    f = open(("Raw_"+filename+".txt"), "w")

    f.write(rawtext)

    f.close()

    #write keywords to to a .txt file

    f = open(filename+"_Keywords.txt", "w")

    for key in keywords:
        f.write(key+"; ")

    f.close()

#This function creates a list of compound places to iterate through for locational checking.
def multiwordplace(POStext):
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
def geolocate(listPlaces):
    #Using Geopy for geolocations
    geolocator = GeoNames(username="dan_laden")
    geolocations = []
    queue = multiprocessing.Queue()
    for loc in listPlaces:
        p = multiprocessing.Process(target=geoLocate, args=(loc[0], queue))
        p.start()

    time.sleep(20)#Wait till everything finishes

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

def geoLocate(location, queue):
    geo = geolocator.geocode(location, timeout=20)
    if not geo == None:
        if not "MT" in geo.address:
            locMT = location+ " MT"
            geo = geolocator.geocode(locMT, timeout=20)
        if not geo == None and "MT" in geo.address:
            queue.put(geo)
#End of functions for data parsing
#########################

#########################
# NOTE Start of main code
rawFiles = {}
argc = 1
if(argc == len(sys.argv)):
    print("Please include files to parse")
    exit()
while(argc<sys.argc):#Opening the file and putting it through the PDF reader.
    filepath = "source/"+sys.argv[argc]
    f = open(filepath, 'rb')
    rawText = readText(PyPDF2.PdfFileReader(f))
    rawFiles[sys.argv[argc]] = rawText
    argc+=1


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
#########################
