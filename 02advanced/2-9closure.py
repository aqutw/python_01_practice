def g():
    print 'g()...'

def f():
    print 'f()...'
    return g

h = f()
h()

#Now, move g into f
def f2():
    print 'f2()...'
    def g2():
        print 'g2()...'
    return g2

print '-------'

#notice:
def count():
    fs = []
    for i in range(1, 4):
        def f0():
             return i*i
        fs.append(f0)
    return fs

a, b, c = count()
print a(), b(), c() #will be 9, 9, 9 (not 1, 4, 9)

print '---My FIX----'
def count():
    fs = []
    for i in range(1, 4):
        def f0():
             return i*i
        fs.append(f0()) #<------see 
    return fs

print count()

print '----official answer----'
def count():
    fs = []
    for i in range(1, 4):
        def f(j): #wrap one more function and pass j into inner g function
            def g():
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()
