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
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk  import FreqDist
import graphene


class Query(graphene.ObjectType):
  hello = graphene.String(description='A typical hello world')

  def resolve_hello(self, info):
    return 'Hello world!'

print("Test File")

f = open("source/This-House-of-Sky-1-5.pdf", 'rb')

pdfReader = PyPDF2.PdfFileReader(f)
text = ""

page = pdfReader.getPage(0)

for i in range(0, pdfReader.getNumPages()):
    print("==========================\n=\tPage "+(str)(i+1)+"\n==========================")
    page = pdfReader.getPage(i)
    text = text + page.extractText()
    print(page.extractText())

translate_table = dict((ord(char), None) for char in string.punctuation)
text = text.translate(translate_table)
print(text)
print("==========================\n=\tWithout stop removal "+(str)(len(text.split()))+"\n==========================")

stoplist = set(stopwords.words('english'))

tokenized_set = word_tokenize(text.lower())
tokenized_sent_nostop = [token for token in tokenized_set if token not in stoplist]

print(tokenized_sent_nostop)
print("==========================\n=\tWith stop removal and .lower "+(str)(len(tokenized_sent_nostop))+"\n==========================")

tokenized_set = word_tokenize(text)
tokenized_sent_nostop = [token for token in tokenized_set if token not in stoplist]
freq_set = FreqDist(tokenized_set)

print(tokenized_sent_nostop)
print("==========================\n=\tWith stop removal and no .lower "+(str)(len(tokenized_sent_nostop))+"\n==========================")
print(freq_set)
print(freq_set.most_common(50))


print("\n\n\n\n\n\n\n\n")



schema = graphene.Schema(query=Query)
result = schema.execute('{ hello }')
print(result.data['hello'])
