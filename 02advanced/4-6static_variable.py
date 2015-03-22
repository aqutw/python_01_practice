class Person(object):
    address = 'Earth' #<-- static
    def __init__(self, name):
        self.name = name

print Person.address # => Earth
p1 = Person('Bob')
p2 = Person('Alice')
print p1.address # => Earth
print p2.address # => Earth
Person.address = 'Cosmos'
print p1.address 
print p2.address

p1.address = 'Cosmos2' #test...
print p1.address #Cosmos2
print p2.address #Cosmos

class Klass(object):
    count = 0
    def __init__(self):
        Klass.count+=1 #MUST use Klass (cannot use self. cannot use 'empty.'

k1 = Klass()
k2 = Klass()
print Klass.count
