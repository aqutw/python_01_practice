class Student(object):
    __slots__ = ('name', 'gender', 'score')
    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score


s = Student('Bob', 'male', 59)
s.name = 'Tim' # OK
s.score = 99 # OK
try:
    s.grade = 'A' # throw Error
except:
    print 'cannot setter .grade'

print '---do Task---'
class Person(object):
    __slots__ = ('name', 'gender')
    def __init__(self):
        pass

class Student0(Person):
    __slots__ = ('score')
    def __init__(self):
        super(Student0, self).__init__()

s0 = Student0()
s0.name = 'Adam'
s0.gender = 'male'
s0.score = 70
print s0.name
print s0.gender
print s0.score

print '---official answer http://www.imooc.com/code/6256 '
