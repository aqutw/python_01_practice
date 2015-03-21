# -*- coding: utf-8 -*-
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print d.values()
# [85, 95, 59]
for v in d.values():
    print v

for v in d.itervalues(): #itervalues() saves more memory of computer than values()
    print v

#for 循环可作用的迭代对象远不止 list，tuple，str，unicode，dict等，任何可迭代对象都可以作用于for循环，而内部如何迭代我们通常并不用关心。

print '---do Task---'
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
dv = d.values()
total = 0.0 # !!! for float, CANNOT use 0 !!!
for v in dv:
    total+=v

print total/len(dv) #Btw, len(dv)==len(d) in python's way
print len(d)
    

print '---official answer---'
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for v in d.itervalues():
    sum = sum + v
print sum / len(d)
