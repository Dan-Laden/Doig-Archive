#################################
# author@ Daniel Laden          #
# email@ dthomasladen@gmail.com #
#################################

print("Test File")#This is only a test files this shouldn't be used for production
import time
start_time = time.time()

import os #ref doc: https://docs.python.org/3.6/library/os.html
import sqlite3 # ref doc: https://docs.python.org/3/library/sqlite3.html
from nltk  import FreqDist

#This class is meant to hold three things rather than having these in a list in the dictionaries
#source is the file name from where the keyword is found, and occurences are the number of times
#that keyword shows up in the source
class Relation:
    def __init__(self, inSource, inKeyword, inOccurrences):
        self.source = inSource
        self.keyword = inKeyword
        self.occurrences = inOccurrences

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

#This function builds a dictionary of relations using a dictionary {keyword: Relation Datastructure}
def buildRelations(f):
    filename = os.path.basename(f.name)#Get the basename of the file

    keywords = f.readline()
    splitKeys = keywords.split("; ")
    freq_set = FreqDist(splitKeys)#split into tokens and create a frequency distribution

    relation_dic = {}

    for word in freq_set:
        if freq_set[word] > 1:#Remove anything that's not mentioned that much
            relation_dic[word] = Relation(filename, word, freq_set[word])

    return relation_dic

#This function crates another dictionary of {"source-keyword": Weight Datastructure}
#it will look at keys in two dictionaries and find where they are matching up then create a weight relation
#for how strongly they are connected
def compareRelations(d1, d2):
    relation_sql = {}
    for key1 in d1:
        for key2 in d2:
            if key1 == key2:
                tag = d1[key1].source + "-" + key1
                relation_sql[tag] = ConnectedRelation(d1[key1].source, key1, d2[key2].source, computeWeight(d1[key1].occurrences, d2[key2].occurrences))

    return relation_sql

#This function computes the weight obviously but it does it by taking the difference of value 1 and value 2 subtracting
#it from the source value (v1) and then dividing it by two. TODO: I might normalize it all to be between 1 and 0
def computeWeight(v1, v2):
    holder = v1 - v2
    if holder < 0:
        holder = -holder
    holder = (v1 - holder)
    return holder

def fillDB(d1):
    connection = sqlite3.connect("relation.db")
    cursor = connection.cursor()

    #For cleaning the database for testing
    cursor.execute("""DROP TABLE employee;""")

    for key in d1:
        sql_addto = """INSERT INTO relations (SourceFile, Keyword, RelatedFile, Weight)
        VALUES ('{0}', '{1}', '{2}', '{3}');""".format(d1[key].source, d1[key].keyword, d1[key].related, d1[key].weight)
        print(sql_addto)
        cursor.execute(sql_addto)

    # necessary for saving changes made
    connection.commit()

    connection.close()

file1 = open("source/ECrelationtest.txt", "r")
file2 = open("source/HSrelationtest.txt", "r")

rel_arr1 = buildRelations(file1)
rel_arr2 = buildRelations(file2)

related_db = compareRelations(rel_arr1, rel_arr2)

fillDB(related_db)

print("--- %s seconds ---" % (time.time() - start_time))
#########################
#resources used for code so far
#
# https://stackoverflow.com/questions/323515/how-to-get-the-name-of-an-open-file
# https://www.python-course.eu/sql_python.php
# https://stackoverflow.com/questions/4709310/python-string-formatting-reference-one-argument-multiple-times
# https://stackoverflow.com/questions/47458189/sqlite3-operationalerror-no-such-column-but-im-not-asking-for-a-column
#########################
