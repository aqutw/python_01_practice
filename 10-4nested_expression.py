print [m + n for m in 'ABC' for n in '123']

print '---do Task---'
print '---my way---'
print [ x*100+y*10+z for x in xrange(1,10) for y in xrange(0, 11) for z in xrange(0, 11) if x*10+y==z*10+y and x*100+y*10+z<1000 ] #has BUG!! ex: 201 is invalid

print [ x*100+y*10+z for x in xrange(1,10) for y in xrange(0, 11) for z in xrange(0, 11) if str(x)+str(y)==str(z)+str(y) and x*100+y*10+z<1000 ]  #why 201 still?

print str(2)+str(0)==str(1)+str(0) #...this is False


print [ x*100+y*10+z for x in xrange(1,10) for y in xrange(0, 11) for z in xrange(0, 11) if x==z ] #WHY still wrong??

print '---official answer---'
print [100 * n1 + 10 * n2 + n3 for n1 in range(1, 10) for n2 in range(10) for n3 in range(10) if n1==n3] #ordered


print '---others answer (goood)---'
print [int(m + n + m) for m in'123456789' for n in '1234567890'] #un-ordered
