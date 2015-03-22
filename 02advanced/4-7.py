print '--do Task--'
class Person(object):
    __count = 0
    def __init__(self, name):
        Person.__count = Person.__count + 1
        self.name = name
        print Person.__count #can access

p1 = Person('Bob')
p2 = Person('Alice')

#print Person.__count #cannot access


class Klass(object):
    __count = 0
    def __init__(self):
        Klass.__count+=1 #MUST use Klass (cannot use self. cannot use 'empty.'
        print '__init__:', Klass.__count #can access

k1 = Klass()
k2 = Klass()
#print Klass.__count #cannot access

