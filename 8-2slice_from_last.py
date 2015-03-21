L = ['Adam', 'Lisa', 'Bart', 'Paul']

print L[-2:]
print L[:-2]
print L[-3:-1], 'NO Paul!!' # Lisa, Bart (no Paul!!!)
print L[-4:-1:2]

print '---do Task---'
a = range(1,101)
print a[-10:] # should be 90 91 92 ... 100
n = -51+5
a2 = a[n::5] #should be 50 55 60 65 ... 100
print a2
print len(a2) #should be 10

print '---official answer--'
L = range(1, 101)
print L[-10:]
print L[-46::5]
