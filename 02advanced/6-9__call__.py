f = abs
print f.__name__
print f(-123)

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend): #<--friend is the parameter of __call__, not attribute
        print 'My name is %s...' % self.name
        print 'My friend is %s...' % friend

p = Person('Bob', 'male')
p('Tim')


print '---do Task--'
print '#my practice'
class Fib(object):
    def __init__(self): #we don't need write __init__ as well
        return

    def __call__(self, n):
        self.lst = []
        max_n = n
        while(n>0):
            _n = max_n - n + 1
            result = self.calc(_n)
            self.lst.append( result )
            n-=1
        return self.lst #<---- add this line

    def calc(self, n):
        if n==1: return 0
        elif n==2: return 1
        else:
            return self.calc(n-2) + self.calc(n-1)

    def __str__(self):
        return str( self.lst )

    __repr__ = __str__

    def __len__(self):
        return len(self.lst)

f = Fib()
print f(10)

print '#official answer'
class Fib2(object):
    def __call__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        return L

f = Fib2()
print f(10)
