print type(5)

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name

stu = Student('Bob', 'Male', 88) 
print type(stu)

print dir(6)
print dir(stu)

s = stu
print getattr(s, 'name') # return name's value if have
setattr(s, 'name', 'Adam') #set name's value
print getattr(s, 'name') # return name's value again
print s.name
try:
    getattr(s, 'age')
except:
    print 'No age!!!'
print getattr(s, 'age', 20) #default value is 20 if no age



