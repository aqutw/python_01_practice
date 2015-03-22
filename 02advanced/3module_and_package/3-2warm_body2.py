import os
#...or...
import os.path
from os import path
from os.path import isdir, isfile

print os.path.isdir('.')
print os.path.isdir('/')
print os.path.isfile('.')
print os.path.isfile('/')

print os.path.isdir(r'C:\Windows')
print os.path.isfile(r'C:\Windows\notepad.exe')


print '---do Task---'
from os.path import isdir,isfile

print isdir(r'/data/webroot/resource/python')
print isfile(r'/data/webroot/resource/python/test.txt')
