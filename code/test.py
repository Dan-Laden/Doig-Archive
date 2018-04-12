#
#author@ Daniel Laden
#email@ dthomasladen@gmail.com
#
#resources used for code so far
#
# https://stackoverflow.com/questions/15547409/how-to-get-rid-of-punctuation-using-nltk-tokenizer
# https://github.com/nltk/nltk/wiki/Frequently-Asked-Questions-(Stackoverflow-Edition)


import nltk, PyPDF2
import string
import re
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk  import FreqDist
#import difflib Library that can compare differences in strings
import graphene


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

print("Test File")

f = open("source/This-House-of-Sky-1-5.pdf", 'rb')

pdfReader = PyPDF2.PdfFileReader(f)
text = ""

page = pdfReader.getPage(0)

for i in range(0, pdfReader.getNumPages()):
#    print("==========================\n=\tPage "+(str)(i+1)+"\n==========================")
    page = pdfReader.getPage(i)
    text = text + page.extractText()
#    print(page.extractText())

translate_table = dict((ord(char), None) for char in string.punctuation)
text = text.translate(translate_table)

#print(text)
#print("==========================\n=\tWithout stop removal "+(str)(len(text.split()))+"\n==========================")

stoplist = set(stopwords.words('english'))

tokenized_set_lower = word_tokenize(text.lower())
tokenized_set_nostop_lower = [token for token in tokenized_set_lower if token not in stoplist]

#print(tokenized_sent_nostop_lower)
#print("==========================\n=\tWith stop removal and .lower "+(str)(len(tokenized_sent_nostop_lower))+"\n==========================")

tokenized_set = word_tokenize(text)
tokenized_set_nostop = [token for token in tokenized_set if token not in stoplist]
freq_set = FreqDist(tokenized_set_nostop)

#print(tokenized_set_nostop)
#print("==========================\n=\tWith stop removal and no .lower "+(str)(len(tokenized_set_nostop))+"\n==========================")
print(freq_set)
print(freq_set.most_common(50))

POStext = nltk.pos_tag(tokenized_set_nostop)
POStextL = nltk.pos_tag(tokenized_set_nostop_lower)


#Testing for to see what's grabbed from parts of speech. Without Removal of non-ASCII Characters
print("\n\n"+(str)(POStext))
print("\n\n"+(str)(POStextL))

#Testing with removing ASCII or UNICODE


textASCNP = stripNonAlphaNumASCII(text)
textASCNPL = stripNonAlphaNumASCII(text.lower())

tokenized_set_ASCII = word_tokenize(textASCNP)
tokenized_set_nostop_ASCII = [token for token in tokenized_set_ASCII if token not in stoplist]
tokenized_set_lower_ASCII = word_tokenize(textASCNPL)
tokenized_set_nostop_lower_ASCII = [token for token in tokenized_set_lower_ASCII if token not in stoplist]

POStextASCII = nltk.pos_tag(tokenized_set_nostop_ASCII)
POStextASCIIL = nltk.pos_tag(tokenized_set_nostop_lower_ASCII)
print("\n\n"+(str)(POStextASCII))
print("\n\n"+(str)(POStextASCIIL))

print("\n\n"+textASCNP)
print("\n\n"+textASCNPL)
print("\n\n"+textASCNP.lower()==textASCNPL)#should be true?








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
