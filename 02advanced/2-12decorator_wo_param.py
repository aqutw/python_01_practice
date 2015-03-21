def log(f):
    #def fn(x): #original
    def fn(*args, **kw):  #<-------see parameters here
        print 'call ' + f.__name__ + '()...'
        #return f(x) #original
        return f(*args, **kw)
    return fn

@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10) #works originally

@log
def add(x, y):
    return x + y
print add(1, 2) #works


print '----official answer----'
import time
def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw) #TODO why need * here? AND what is **kw (Is there ***kwmore  ****kwmoremore?)
        t2 = time.time()
        print 'call %s() in %fs' % (f.__name__, (t2 - t1))
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)
