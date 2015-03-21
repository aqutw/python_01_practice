s = set([1,2,3,]) #oh, we can add one more dot at last element
s.add(4)
print s
s.add(4)
print s #no error AND nothing happen

s.remove(2)
print s
#s.remove(999) #throw error



print '===do Task===='
s = set(['Adam', 'Lisa', 'Paul'])
a = ['Adam', 'Lisa', 'Bart', 'Paul']
for v in a:
    if v in s:
        s.remove(v)
    else:
        s.add(v) 

print s
