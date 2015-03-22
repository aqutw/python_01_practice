class Person(object):
    def __init__(self, name):
        self.name = name
        self._title = 'Mr'
        self.__job = 'Student'


p = Person('Bob')
print p.name
# => Bob
print p._title
# => Mr

try:
    print p.__job
except:
    print 'Cannot access __job'






class Person2(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
        self.__specialattr__ = score

p = Person2('Bob', 59)

print p.name
print p.__specialattr__
try:
    print p.__score
except:
    print 'Cannot access __score'
