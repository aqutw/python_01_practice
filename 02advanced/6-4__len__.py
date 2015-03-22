class Students(object):
    def __init__(self, *args):
        self.names = args
    def __len__(self):
        return len(self.names)


ss = Students('Bob', 'Alice', 'Tim')
print len(ss)

print '---do Task--'
print '#my practice'
class Fib(object):
    def __init__(self, n):
        self.lst = []
        max_n = n
        while(n>0):
            _n = max_n - n + 1
            result = self.calc(_n)
            self.lst.append( result )
            n-=1

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

f = Fib(10)
print f
print len(f)

print '#official answer'
class Fib2(object):
    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        self.numbers = L

    def __str__(self):
        return str(self.numbers)

    __repr__ = __str__

    def __len__(self):
        return len(self.numbers)

f = Fib2(10)
print f
print len(f)
