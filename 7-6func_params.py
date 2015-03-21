def my_power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print my_power(5)
print my_power(5, 3)

print '----do Task----'
def greet(name='world'):
    print 'Hello, ' + name + '.'
print greet()
print greet('Bart')
