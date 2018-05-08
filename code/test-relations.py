#################################
# author@ Daniel Laden          #
# email@ dthomasladen@gmail.com #
#################################

print("Test File")#This is only a test files this shouldn't be used for production
import time
start_time = time.time()

import os

class Relation:
    def __init__(self, inSource, inKeyword, inOccurrences):
        self.source = inSource
        self.keyword = inKeyword
        self.occurrences = inOccurrences

def buildRelations(File):
