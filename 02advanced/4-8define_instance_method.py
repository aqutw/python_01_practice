class Person(object):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


p = Person('Tony')
print p.get_name()

print '---do Task---'
class Person2(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 80:
            return 'A'
        if self.__score >= 60:
            return 'B'
        return 'C'

p1 = Person2('Bob', 90)
p2 = Person2('Alice', 65)
p3 = Person2('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()
