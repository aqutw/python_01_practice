class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender) #<--add this line (No need `self` as 1st parameter of __init__)
        self.score = score

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')

print 'p'
print isinstance(p, Person) #T
print isinstance(p, Student) #F
print isinstance(p, Teacher) #F
print 's'
print isinstance(s, Person)
print isinstance(s, Student)
print isinstance(s, Teacher)
print 't'
print isinstance(t, Person)
print isinstance(t, Student)
print isinstance(t, Teacher)
print isinstance(t, object)
