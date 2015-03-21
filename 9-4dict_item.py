d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print d.items()

for k, v in d.items():
    print k, ':', v

for k, v in d.iteritems():
    print k, ':', v

print '---do Task--'
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
total = 0.0
for k, v in d.iteritems():
    print k, ':', v
    total+=v
print 'average', ':', total/len(d)



