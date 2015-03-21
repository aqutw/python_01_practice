import math

def is_odd(x):
    return x % 2 == 1
print filter(is_odd, [1, 4, 6, 7, 9, 12, 17])

def is_not_empty(s):
    return s and len(s.strip()) > 0
print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])

print 'cabcdc'.strip('c')
print 'xabcdc'.strip('c')
print 'cabcdx'.strip('c')
print '\r\n\n\ncabcdx\t'
print '\r\n\n\ncabcdx\t'.strip()

def f(n):
    r = int(math.sqrt(n))
    return r*r==n
print filter(f, range(1,101))
