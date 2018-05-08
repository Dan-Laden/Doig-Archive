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

def buildRelations(f):
    filename = os.path.basename(f.name)

    keywords = f.readline()
    splitKeys = keywords.split("; ")
    freq_set = FreqDist(splitKeys)

    relation_arr = []

    for word in freq_set:
        if freq_set[word] > 9:
            relation_arr.append(Relation(filename, word, freq_set[word]))

    return relation_arr


file = open("testkey.txt", "r")

rel_arr = buildRelations(file)

print(rel_arr[4].source + ", " + rel_arr[4].keyword + ", " + (str)(rel_arr[4].occurrences))

print("--- %s seconds ---" % (time.time() - start_time))
#########################
#resources used for code so far
#
# https://stackoverflow.com/questions/323515/how-to-get-the-name-of-an-open-file
#########################
