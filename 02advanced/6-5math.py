def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, other):
        return Rational(self.p * other.q + self.q * other.p, self.q * other.q)
    def __sub__(self, other):
        return Rational(self.p * other.q - self.q * other.p, self.q * other.q)
    def __mul__(self, other):
        return Rational(self.p * other.p, self.q * other.q)
    def __div__(self, other):
        return Rational(self.p * other.q, self.q * other.p)
    def __str__(self):
        #return '%s/%s' % (self.p, self.q)
        g = gcd(self.p, self.q)
        return '%s/%s' % (self.p / g, self.q / g)
    __repr__ = __str__

r1 = Rational(1, 3)
r2 = Rational(1, 2)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2
