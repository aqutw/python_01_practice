class Person(object):
    def __init__(self, name, gender, **kw): #add , **kw
        self.name = name
        self.gender = gender
        for k, v in kw.iteritems(): #add this line
            setattr(self, k, v) #add this line

p = Person('Bob', 'Male', age=18, course='Python') #see , age=18, course='Python'
print p.age #we got the result
print p.course #we got the result
