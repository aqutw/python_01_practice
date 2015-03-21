d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print 'Adam:', d['Adam']
print 'Lisa:', d['Lisa']
print 'Bart:', d['Bart']

print d.get('Paul')

if 'Paul' in d:
    print d['Paul']
else:
    print 'no Paul'

