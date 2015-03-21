print range(1, 11)

a = []
for v in xrange(1,11):
    a.append(v*v)
print a

print 'More shorten way....'
print [x * x for x in range(1, 11)]

print '---do Task---'
print range(1,100,2)

print [ x*(x+1) for x in range(1,100,2) ]
