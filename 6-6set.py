# -*- coding: utf-8 -*-
#set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。

s = set(['A', 'B', 'C', 'C', 'repeatMe', 'repeatMe'])
print s #set's elements will be unique

a = ['a','b','c']
s = set(a) #yes, i can pass List to Set
print s
