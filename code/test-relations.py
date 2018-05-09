#################################
# author@ Daniel Laden          #
# email@ dthomasladen@gmail.com #
#################################

print("Test File")#This is only a test files this shouldn't be used for production
import time
start_time = time.time()

import os
from nltk  import FreqDist

class Relation:
    def __init__(self, inSource, inKeyword, inOccurrences):
        self.source = inSource
        self.keyword = inKeyword
        self.occurrences = inOccurrences

class Weight:
    def __init__(self, inSource, inWeight):
        self.source = inSource
        self.weight = inWeight

def buildRelations(f):
    filename = os.path.basename(f.name)

    keywords = f.readline()
    splitKeys = keywords.split("; ")
    freq_set = FreqDist(splitKeys)

    relation_dic = {}

    for word in freq_set:
        if freq_set[word] > 9:
            relation_dic[word] = Relation(filename, word, freq_set[word])

    return relation_dic

def compareRelations(d1, d2):
    relation_sql = {}
    for key1 in d1:
        print(key1+"\n-----------")
        for key2 in d2:
            print(key2+"\n_________")
            if key1 == key2:
                tag = d1[key1].source + "-" + key1
                relation_sql[tag] = Weight(d2[key2].source, computeWeight(d1[key1].occurrences, d2[key2].occurrences))

    return relation_sql


def computeWeight(v1, v2):
    holder = v1 - v2
    if holder < 0:
        holder = -holder
    holder = (v1 - holder)/2
    return holder


file1 = open("testkey.txt", "r")
file2 = open("testwrite.txt", "r")

rel_arr1 = buildRelations(file1)
file1 = open("testkey.txt", "r")
rel_arr3 = buildRelations(file1)

weight_db = compareRelations(rel_arr1, rel_arr3)

for key in weight_db:
    print(key+": source "+weight_db[key].source+", weight "+ (str)(weight_db[key].weight)+"\n___________")

#print(rel_arr[4].source + ", " + rel_arr[4].keyword + ", " + (str)(rel_arr[4].occurrences))

print("--- %s seconds ---" % (time.time() - start_time))
#########################
#resources used for code so far
#
# https://stackoverflow.com/questions/323515/how-to-get-the-name-of-an-open-file
#########################
