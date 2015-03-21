def log(prefix):
    def log_decorator(f):
        def fn(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)
        return fn 
    return log_decorator

@log('DEBUG')
def test():
    pass #same as `return`; same as `return None`
print test()

print '---do Task----'
print '#official answer'
import time
def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print 'call %s() in %f %s' % (f.__name__, t, unit)
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)

print '#my try'
def performance(unit):
    def performance_deco(f):
        def fn(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()

            if unit=='ms':
                t1 = t1*1000
                t2 = t2*1000

            print 'call %s() in %fs' % (f.__name__, (t2 - t1))
            return r
        return fn #REMEBER return fn
    return performance_deco

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)


