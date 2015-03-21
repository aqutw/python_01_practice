print 'ABCDEFG'[:3]
print 'ABCDEFG'[-3:]
print 'ABCDEFG'[::2]

print 'abc'.upper()
print 'XYZ'.lower()

print '----do Task----'
def only_first_upper(s):
    return s[0:1].upper() + s[1:]

print only_first_upper('abc') #should be Abc
print only_first_upper('aBc') #should be ABc

print '--official answer--'
def firstCharUpper(s): #<--Let me guess pythoner like camelCase.
    return s[0].upper() + s[1:]
print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')
