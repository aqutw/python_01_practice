def f(x,y):
    return x+y

print reduce(f, [1,3,5,7,9])

print reduce(f, [1,3,5,7,9], 100)

def my_func(x,y):
    return x*y
print reduce(my_func, [2,4,5,7,12])

