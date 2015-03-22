# -*- coding: utf-8 -*-
class Person(object):
    count = 0
    @classmethod
    def how_many(cls_any_name_you_want): # 类方法的第一个参数将传入类本身，通常将参数名命名为 cls，上面的 cls.count 实际上相当于 Person.count。
        return cls_any_name_you_want.count
    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1

print Person.how_many()
p1 = Person('Bob')
print Person.how_many()


print '----do Task----'
class Person2(object):
    __count = 0
    @classmethod
    def how_many(cls):
        return cls.__count
    def __init__(self, name):
        self.name = name
        Person2.__count = Person2.__count + 1

print Person2.how_many()
p1 = Person2('Bob')
print Person2.how_many()
