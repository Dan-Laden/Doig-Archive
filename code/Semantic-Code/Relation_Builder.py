#################################
# author@ Daniel Laden          #
# email@ dthomasladen@gmail.com #
#################################

print("Main File")
import time
start_time = time.time()

import sqlite3 #ref doc: https://docs.python.org/3/library/sqlite3.html
import os #ref doc: https://docs.python.org/3.6/library/os.html
import string #ref doc: https://docs.python.org/3.3/library/string.html?highlight=string#module-string
import glob #ref doc: https://docs.python.org/3.7/library/glob.html#module-glob
import re #ref doc: https://docs.python.org/3/library/re.html#re.ASCII

#########################
#Main classes for relation building

#This class is meant to hold three things rather than having these in a list in the dictionaries
#source is the file name from where the keyword is found, and occurences are the number of times
#that keyword shows up in the source
class Relation:
    def __init__(self, inSource, inKeyword, inOccurrences, inPages):
        self.source = inSource
        self.keyword = inKeyword
        self.occurrences = inOccurrences
        self.pages = inPages


#Much like the class above this was made to avoid using lists inside of dictionaries
#Source is the file that has the same keyword as the file we're looking at
#Keyword is the specific keyword being related between Source and Related
#Related is the file that has a connection to Source by keyword
#Weight is calculated by computeWeight but it's how strong that relation is
class ConnectedRelation:
    def __init__(self, inSource, inKeyword, inRelated, inWeight):
        self.source = inSource
        self.keyword = inKeyword
        self.related = inRelated
        self.weight = inWeight

#End of class for relation building
#########################

#########################
#Main functions for relation building

#This method fills the database with the relations created in makeRelations
def fillRelationDB(relationList):
    connection = sqlite3.connect("relation.db")
    cursor = connection.cursor()

    try:
        #For cleaning the database for testing
        cursor.execute("""DELETE FROM RELATIONS;""")

    #This  is for if the database is new and a table for the items is needed to be created.
    except sqlite3.OperationalError:
        print("Detect no previous database, one will be made.")

        sql_createtb = """CREATE TABLE `RELATIONS` (
        `SourceFile`	TEXT,
        `Keyword`	TEXT,
        `RelatedFile`	TEXT,
        `Weight`	INTEGER
        );"""
        cursor.execute(sql_createtb)

    for relation in relationList:
        sql_addto = """INSERT INTO relations (SourceFile, Keyword, RelatedFile, Weight)
        VALUES ('{0}', '{1}', '{2}', '{3}');""".format(relation.source, relation.keyword, relation.related, relation.weight)
        cursor.execute(sql_addto)

    # necessary for saving changes made
    connection.commit()

    connection.close()

#This function computes the weight by normalizing the two entered in values
def computeWeight(v1, v2):
    R = 0
    if(v1>v2):
        R = v2/v1
    elif(v1<v2):
        R = v1/v2
    else:
        R = 1
    return R

#This function find the Relation objects with the same source as the passed in fileName
def grabRelations(inRelationList, fileName):
    relationList = []
    for relation in inRelationList:
        if fileName == relation.source:
            relationList.append(relation)

    return relationList

#Get the name of the file and then use the converter from Semantic_Enhancement to get the way it's written in the db
def getDBname(path):
    path = path.split("/Keywords/")
    path = path[1]
    path = path.replace("Keywords-", '')
    path = path.replace(".txt", '')
    path = path.replace("-", " ")
    digits = re.findall('\d+', path)#I'm using regular expressions instead of forloops because I think that's faster proformance
    digit = digits[0]
    source = path.replace((" "+digit), "")
    return(path.replace((" "+digit), (", Chapter "+digit)))

#This function takes a list of read in files from the program and creates a "graph" of biconnected ConnectedRelation objects
def makeRelations(relationList):
    connectedList = []
    switcher = 0
    #TODO fix the only using the first chapter from everybook
    #TODO go until relation 2 is after relation 1
    for relation1 in relationList:
        for relation2 in relationList: #This if statement needs to check to make sure the keywords are the same, and the relation1 source is not from the same book as the relation2
            if relation2.source == relation1.source and switcher == 0:
                switcher = 1
            elif relation1.source != relation2.source and relation1.keyword == relation2.keyword and switcher == 1:
                try:
                    weight1 = (int)(relation1.occurrences) * (relation1.pages * 0.1)
                    weight2 = (int)(relation2.occurrences) * (relation2.pages * 0.1)
                    connectedweight = computeWeight(weight2, weight1)
                except:
                    connectedweight = 1

                if(connectedweight >= 0.01):
                    connectedList.append(ConnectedRelation(relation2.source, relation2.keyword, relation1.source, connectedweight))
        switcher = 0

    return connectedList

#End of functions for relation building
#########################

#########################
# NOTE Start of main code


#{filename : keywords, filename : keywords}

#IDEA Use both keywords and geolocations to create the relations because from the item-page it shouldn't matter
# if you click keyword or geolocation the related page should display the same way. Though for the sentiment analysis
# it should be tacked on to the end of the keyword output so when you click on the sentiment mood it can use the same keyword
# php post key

relationList = []
for filepath in os.listdir('output'):
    path_keyword = "output/"+filepath+"/Keywords/*.txt"
    path_geolocation = "output/"+filepath+"/Geolocations/*.txt"
    file_key = glob.glob(path_keyword)
    file_geo = glob.glob(path_geolocation)
    for fullpath_key, fullpath_geo in zip(file_key, file_geo):
        f = open(fullpath_key, 'r')
        g = open(fullpath_geo, 'r')

        #getting the keywordss first
        keywords = f.readline()
        keywordlist = keywords.split('; ')
        keywordlist.pop() #to removed the empty string at the end of the list

        #need the same thing for the Geolocations
        geolocate = g.readline()
        geolist = geolocate.split('; ')
        geolist.pop()

        #combine the two lists
        keywordlist = keywordlist + geolist


        occurenceList ={}
        for keyword in keywordlist:
            keyword = keyword.split("|")
            occurenceList[keyword[0]] = keyword[1]


        chapter = getDBname(fullpath_key)
        conn = sqlite3.connect('items.db')
        c = conn.cursor()
        sqlget = """SELECT Pages from ITEMS
        WHERE ID='{0}';""".format(chapter)
        for row in c.execute(sqlget):
            pages = row[0]
        conn.close()

        for keyword in occurenceList:
            relationList.append(Relation(chapter, keyword, occurenceList[keyword], pages))

print("--- %s seconds to create all relations ---" % (time.time() - start_time))

#NOTE start of relation building
fillRelationDB(makeRelations(relationList)) #creates the relations and fills a database with those relations

seconds = round(time.time() - start_time)
minutes = 0
hours = 0
if seconds > 60:
    minutes = int(seconds/60)
    seconds = seconds - (minutes * 60)
if minutes > 60:
    hours = int(minutes/60)
    minutes = minutes - (hours * 60)
print("--- %s hours ---\n--- %s minutes ---\n--- %s seconds ---" % (hours, minutes, seconds))

#End of main code
#########################

#########################
#resources used for code so far
#
#https://www.quora.com/How-do-I-read-mutiple-txt-files-from-folder-in-python#
#########################
