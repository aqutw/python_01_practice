def f():
    print 'call f()...'
    def g():
        print 'call g()...'
    return g

x = f() #execute f, and pass g to x
print x
x()



def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum
x = calc_sum([1,2,3,4])
print x()


print '---do Task---'
def calc_prod(lst):
    def f():
        n = 1
        for v in lst:
            n*=v
        return n
    return f

f = calc_prod([1,2,3,4])
print f()
