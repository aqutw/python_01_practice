for x in [ 0,1,2,3,4,5,6,7,8,9 ]:
    for y in [ 0,1,2,3,4,5,6,7,8,9 ]:
        if x < y:
            print x*10+y,

print ""

for x in [ 0,1,2,3,4,5,6,7,8,9 ]:
    for y in [ 0,1,2,3,4,5,6,7,8,9 ]:
        if x < y:
            print str(x) + str(y), # In python, we cannot use str(x) + y (!?). (If so, ) we need cast y from integer to string.

#see also http://stackoverflow.com/questions/961632/converting-integer-to-string-in-python


print range(0,4) # [0,1,2,3]

for x in xrange(0, 10):
    for y in xrange(0, 10):
      if x < y:
        print x*10+y,

#see also http://stackoverflow.com/questions/493386/how-to-print-in-python-without-newline-or-space for print
