def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

def my_abs2(x):
    return x if x>=0 else -x #one of python's ternary condition, there are more ways on http://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator

def return_None():
    return None
def return_None2():
    return

def return_None3():
    print '...your code...'

print my_abs(-10)
print my_abs(10)
print my_abs2(-10)
print my_abs2(10)
print return_None
print return_None2
print return_None3

def square_of_sum(List):
    s=0
    for v in List:
        s+=v*v
    return s

print square_of_sum([1,2,3])
