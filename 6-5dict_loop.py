d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for k in d:
    print k+":", d[k] #use dot, then we do not need cast integer to string

for k in d:
    print k+": "+str(d[k])

for k in d:
    print k+": "+d[k].__str__()


print 'COMPARE WITH List, see v:'
a = ['a','b','c']
for v in a:
    print v
