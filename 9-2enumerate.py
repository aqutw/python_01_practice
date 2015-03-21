a = ['a','b','c','d']
for k, v in enumerate(a):
    print k, '-', v


my_list = [('a','b'), ('c','d'), ('e', 'f')]
for v1, v2 in enumerate(my_list):
    print v1, '#', v2 # still key-value, NOT value1, value2

for v in enumerate(my_list):
    print v[0], '#', v[1]

for v in enumerate(a):
    print v[0], '-', v[1]

print '-----end of test----'

print zip([1,2,3], ['A','B','C'])

print '----do Task---'
a = ['Adam', 'Lisa', 'Bart', 'Paul']
a2 = zip(range(1,len(a)+1), a)
print a2
for k, v in enumerate(a2):
    print v[0], '-', v[1].lower()

