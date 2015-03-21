def f1(x):
    return x*2

def new_fn(f):
    def fn(x):
        print 'decorate: call ' + f.__name__ + '()' #we decorate at this line
        return f(x)
    return fn

h = new_fn(f1) # way1
print h(5)

f1 = new_fn(f1) # way2 (override f1)
print f1(5)

#PS:
#new_fn = 3 #bad. because python's variable do not have dollar as prefix like PHP, so the naming will be override original function name
#print new_fn #---> show integer 3

#########################
@new_fn #<---override f1B WITH new_fn quickly
def f1B(x):
    return x*2

print f1B(5)
