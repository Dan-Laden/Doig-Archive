#################################
# author@ Daniel Laden          #
# email@ dthomasladen@gmail.com #
#################################

print("Test File")#This is only a test files this shouldn't be used for production

import nltk #ref doc: http://www.nltk.org/howto/index.html
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk  import FreqDist
import string #ref doc: https://docs.python.org/3.3/library/string.html?highlight=string#module-string
import re #ref doc: https://docs.python.org/3/library/re.html#re.ASCII
import PyPDF2 #ref doc: https://pythonhosted.org/PyPDF2/
import difflib #Library that can compare differences in strings ref doc: https://docs.python.org/3.3/library/difflib.html?highlight=difflib#module-difflib
import graphene #ref doc: http://docs.graphene-python.org/en/latest/quickstart/

stoplist = set(stopwords.words('english'))#set of all stopwords in english thanks to nltk

#########################
#GraphQL testing classes
class Query(graphene.ObjectType):
  hello = graphene.String(description='A typical hello world')

  def resolve_hello(self, info):
    return 'Hello world!'


class Book(graphene.ObjectType):
    title = graphene.String(description='Title of Book')
    content = graphene.String(description='All words in the book')
    keywords = graphene.String(description='Important metadata for the book')

    chapterlist = graphene.List(graphene.Field(lambda: Chapter))

    def resolve_title(self, info):
        return info.content.get('title')
    def resolve_content(self, info):
        return info.content.get('content')

#class SearchResult(graphene.ObjectType):
#    class Meta:
#        booklist = graphene.List(Book)
#

class Chapter(graphene.ObjectType):
    number = graphene.Int(description='Chapter Number')
    content = graphene.String(description='Words in the chapter')
    keywords = graphene.List(graphene.String)
#End of GraphQL test classes
#########################


#########################
#Main functions for data parsing

#This function removes strange characters that are read in by the PDF reader
def stripNonAlphaNumASCII(text):
    return listToString(re.compile(r'\W+', re.ASCII).split(text))

#This is a function that no longer is necessary but I'm leaving it in the code if it is needed any time later.
#def stripNonAlphaNumUNICODE(text):
#    return re.compile(r'\W+', re.UNICODE).split(text)

#This takes a list and converts is into a string
#This function goes along with stripNonAlphaNumASCII since it returns a list normally
def listToString(list):
    returnStr = ''
    for STR in list:
        returnStr = returnStr +" "+ STR
    return returnStr

#TODO: Optional idea but make it so Diff doesn't print the lines that don't change.
#XXX:Make sure lists are put into this function
#This will check the difference between the two lists
def checkDiff(list1, list2):
    d = difflib.Differ()
    diff = d.compare(list1, list2)
    print ('\n'.join(diff))
#End of functions for data parsing
#########################

#########################
# NOTE Start of main code

#Opening the file and putting it through the PDF reader.
f = open("source/This-House-of-Sky-1-100.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(f)


#Grabbing all the text from the PDF
text = ""
for i in range(0, pdfReader.getNumPages()):
#    print("==========================\n=\tPage "+(str)(i+1)+"\n==========================")
    page = pdfReader.getPage(i)
    text = text + page.extractText()
#    print(page.extractText())


#Removing all the punctuation from the text.
translate_table = dict((ord(char), None) for char in string.punctuation)
text = text.translate(translate_table)

#print(text)
#print("==========================\n=\tWithout stop removal "+(str)(len(text.split()))+"\n==========================")

#We look at two forms here either .lower() the text or leave it with it's capitalzation.
tokenized_set = word_tokenize(text)
tokenized_set_nostop = [token for token in tokenized_set if token not in stoplist]

# NOTE For now it seems like keeping the capitalzation is for the best
#tokenized_set_lower = word_tokenize(text.lower())
#tokenized_set_nostop_lower = [token for token in tokenized_set_lower if token not in stoplist]
#print(tokenized_sent_nostop_lower)
#print("==========================\n=\tWith stop removal and .lower "+(str)(len(tokenized_sent_nostop_lower))+"\n==========================")
#print(tokenized_set_nostop)
#print("==========================\n=\tWith stop removal and no .lower "+(str)(len(tokenized_set_nostop))+"\n==========================")


#Toying with the idea that we can make a freq_set with certain nouns and verbs used in a chapter
#This is here simply to test the functionality of FreqDist TODO will use later
#freq_set = FreqDist(tokenized_set_nostop)
#print(freq_set)
#print(freq_set.most_common(50))

#Parts of Speech ref doc: http://www.nltk.org/book/ch05.html
POStext = nltk.pos_tag(tokenized_set_nostop)
#POStextL = nltk.pos_tag(tokenized_set_nostop_lower)


#Testing for to see what's grabbed from parts of speech. Without Removal of non-ASCII Characters
#print("\n\n"+(str)(POStext))
#print("\n\n"+(str)(POStextL))


#Using this to remove random non-ASCII characters that are from the PDF reader
textASCNP = stripNonAlphaNumASCII(text)
tokenized_set_ASCII = word_tokenize(textASCNP)
tokenized_set_nostop_ASCII = [token for token in tokenized_set_ASCII if token not in stoplist]

# NOTE might use .lower() for something later but for now we have no real reason to.
#textASCNPL = stripNonAlphaNumASCII(text.lower())
#tokenized_set_lower_ASCII = word_tokenize(textASCNPL)
#tokenized_set_nostop_lower_ASCII = [token for token in tokenized_set_lower_ASCII if token not in stoplist]
#POStextASCIIL = nltk.pos_tag(tokenized_set_nostop_lower_ASCII)
#print("\n\n"+(str)(POStextASCIIL))
#print("\n\n"+textASCNPL)
# NOTE for testing purposes only just to see how .lower() with ASCII removal compares
#POStextASCII = nltk.pos_tag(tokenized_set_nostop_ASCII)
#print("\n\n"+(str)(POStextASCII))
#print("\n\n"+(str)(POStextASCII.lower()==POStextASCIIL))#should be true I think? Yes


#putting POS on the list of tokens without stopwords and non-ASCII characters
POStext = nltk.pos_tag(tokenized_set_nostop_ASCII) #for going forward


#keyword generation
keywordsNN = [] #possible idea remove nouns that are less than 3 characters long
keywordsVB = [] #possible idea parse it through a dictionary of all english verbs to get rid of random nouns and false positives
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
        #print(token)
    elif verb.match(token[1]):
        keywordsVB.append(token[0])
        #print(token)


#print("\n\n\n"+(str)(keywordsNN)+"\n\n\n"+(str)(keywordsVB))# Prints out what keywords are grabbed
print("\n\n\n\n\n"+(str)(keywordsNN2chr))


freq_setNN = FreqDist(keywordsNN)
#print("\n\n\n"+(str)(freq_setNN))
#print(freq_setNN.most_common(50))
freq_setVB = FreqDist(keywordsVB)
#print("\n\n\n"+(str)(freq_setVB))
#print(freq_setVB.most_common(50))


#TODO fix the keyword tables.

#End of main code
#########################

#########################
#GraphQL testing and playing around
print("\n\n\n\n\n\n\n\n")

fakeKeys1 = ['Montana', 'Fishing', 'Wildlife']
fakeKeys2 = ['Idaho Falls', 'Troy, Montana', 'Avians']

ch5 = Chapter(number = 5,content=text,keywords=fakeKeys1)
ch2 = Chapter(number = 2,content=text,keywords=fakeKeys2)

book1 = Book(title="Sky House",content=text,)

schema = graphene.Schema(query=Query)
result = schema.execute('{ hello }')
print(result.data['hello'])

print("\n\n\n")
print("===Test for GraphQL===")
print("Chapter: "+(str)(ch5.number)+"\n")
#print("===Content===\n"+ch5.content+"\n")
print("===Keywords===\n")
for key in ch5.keywords:
    print(key)
print("\n")
#End of GraphQL testing
#########################

#########################
#resources used for code so far
#
# https://stackoverflow.com/questions/15547409/how-to-get-rid-of-punctuation-using-nltk-tokenizer
# https://github.com/nltk/nltk/wiki/Frequently-Asked-Questions-(Stackoverflow-Edition)
# https://programminghistorian.org/lessons/normalizing-data
# https://pymotw.com/2/difflib/
# https://www.guru99.com/python-regular-expressions-complete-tutorial.html
#########################
