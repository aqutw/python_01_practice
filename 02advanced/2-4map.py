def f(x):
    return x*x

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a2 = map(f, a)
print a2
print a

def my_func(s):
    return s[0].upper() + s[1:].lower()
print map(my_func, ['adam', 'LISA', 'barT'])
