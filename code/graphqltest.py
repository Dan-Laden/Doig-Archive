#################################
# author@ Daniel Laden          #
# email@ dthomasladen@gmail.com #
#################################

print("Test File")#This is only a test files this shouldn't be used for production
import time
start_time = time.time()

import graphene #ref doc: http://docs.graphene-python.org/en/latest/quickstart/

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
#GraphQL testing and playing around
# print("\n\n\n\n\n\n\n\n")
#
# fakeKeys1 = ['Montana', 'Fishing', 'Wildlife']
# fakeKeys2 = ['Idaho Falls', 'Troy, Montana', 'Avians']
#
# ch5 = Chapter(number = 5,content=text,keywords=fakeKeys1)
# ch2 = Chapter(number = 2,content=text,keywords=fakeKeys2)
#
# book1 = Book(title="Sky House",content=text,)
#
# schema = graphene.Schema(query=Query)
# result = schema.execute('{ hello }')
# print(result.data['hello'])
#
# print("\n\n\n")
# print("===Test for GraphQL===")
# print("Chapter: "+(str)(ch5.number)+"\n")
# #print("===Content===\n"+ch5.content+"\n")
# print("===Keywords===\n")
# for key in ch5.keywords:
#     print(key)
# print("\n")
#End of GraphQL testing
#########################

print("--- %s seconds ---" % (time.time() - start_time))
