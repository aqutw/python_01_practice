# -*- coding: utf-8 -*-
import json

try:
    f = open('/path/to/file.json', 'r')
    print json.load(f) #任何对象，只要有read()方法，就称为File-like Object，都可以传给json.load()。
except:
    print 'file does not exist.'


print '---my practice----'
class FileLike(object):
    def __init__(self, jsontxt):
        self.__jsontxt = jsontxt
    def read(self): #<--MUST pass self as 1st parameter for every instanceMethod
        return self.__jsontxt

f = FileLike( r'["Tim", "Tony"]' )

print json.load(f)

print '-----official answer---'
class Students(object):
    def read(self):
        return r'["Tim", "Bob", "Alice"]'

s = Students()

print json.load(s)
