# -*- coding: utf-8 -*-
import types
def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

p1 = Person('Bob', 90)
p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
print p1.get_grade()
# => A
p2 = Person('Alice', 65)
try:
    print p2.get_grade()
except:
    print 'ERROR:ATTR ERROR'
# ERROR: AttributeError: 'Person' object has no attribute 'get_grade'
# 因为p2实例并没有绑定get_grade
# 给一个实例动态添加方法并不常见，直接在class中定义要更直观。

print '---do Task---'
class Person2(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person2('Bob', 90)
print '=====p1.get_grade'
print p1.get_grade
print '=====p1.get_grade()'
print p1.get_grade()
