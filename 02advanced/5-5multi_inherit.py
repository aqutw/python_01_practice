# -*- coding: utf-8 -*-
#像这样，D 同时继承自 B 和 C，也就是 D 拥有了 A、B、C 的全部功能。多重继承通过 super()调用__init__()方法时，A 虽然被继承了两次，但__init__()只调用一次：
class A(object):
    def __init__(self, a):
        print 'init A...'
        self.a = a

class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print 'init B...'

class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print 'init C...'

class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print 'init D...'

d = D('d')

print '--do Task---'
class Person(object):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class SkillMixin(object):
    pass

class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'

class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'

class BasketballStudent(BasketballMixin, Student):
    def __init__(self):
        super(BasketballStudent, self).__init__()

class FootballTeacher(FootballMixin, Teacher):
    def __init__(self):
        super(FootballTeacher, self).__init__()

s = BasketballStudent()
print s.skill()
t = FootballTeacher()
print t.skill()

print '---official answer = http://www.imooc.com/code/6248 '
