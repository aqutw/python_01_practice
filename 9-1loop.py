a = range(0,101)

for v in a:
    if v%7==0:
        print v,

print '\n--use xrange--'
for v in xrange(0, 101): # another python's way with xrange
    if v%7==0:
        print v,


