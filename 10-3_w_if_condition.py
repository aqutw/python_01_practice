
print '--wo if--'
print [x * x for x in range(1, 11)]

print '--w if--'
print [x * x for x in range(1, 11) if x % 2 == 0]


print '---do Task---'
#check variable type.... http://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string-in-python

def fn(List):
  return [v.upper() for v in List if isinstance(v, str)]

a = fn(['abc', 'EFd', 3, 0, True, 'xxY'])
print a 
