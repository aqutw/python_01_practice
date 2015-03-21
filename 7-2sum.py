print '====do Task===='
# OMG, python has no for i=0;i<10;i++ !!?? --> use while


# not DRY
a = []
for x in xrange(0,10):
    for y in xrange(0,10):
        n = x*10+y
        print n,
        a.append(n*n)

a.append(100*100)

print sum(a)

# official answer
a = []
x = 1
while x <= 100:
    a.append(x*x)
    x+=1

print sum(a)
