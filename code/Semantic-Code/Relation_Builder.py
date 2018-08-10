#################################
# author@ Daniel Laden          #
# email@ dthomasladen@gmail.com #
#################################

print("Main File")
import time
start_time = time.time()

import sqlite3 #ref doc: https://docs.python.org/3/library/sqlite3.html

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
                weight1 = relation1.occurrences * (relation1.pages * 0.1)
                weight2 = relation2.occurrences * (relation2.pages * 0.1)
                connectedweight = computeWeight(weight2, weight1)
                if(connectedweight >= 0.01):
                    connectedList.append(ConnectedRelation(filenameFix(relation2.source), relation2.keyword, filenameFix(relation1.source), connectedweight))

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

for keywords in keylist:
    for key in keywords:
        if(key[1]>1):
            keywordlist = keywordlist + key[0] + "; "

relationList #list of Related objects


print("--- %s seconds to create all relations ---" % (time.time() - start_time))

#End of main code
#########################
