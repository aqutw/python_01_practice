class Person(object): 
    pass
xiaoming = Person()
xiaohong = Person()
print xiaoming
print xiaohong
print xiaoming == xiaohong

#4-3 start
xiaoming.name = 'Xiao Ming'
xiaoming.gender = 'Male'
xiaoming.birth = '1990-1-1'

xiaohong.name = 'Xiao Hong'
xiaohong.school = 'No. 1 High School'
xiaohong.grade = 2

xiaohong.grade = xiaohong.grade + 1
print xiaoming.gender
print xiaohong.grade


print '---do Task---'
class Person2(object):
    pass
p1 = Person2()
p1.name = 'Bart'

p2 = Person2()
p2.name = 'Adam'

p3 = Person2()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1, lambda p1, p2: cmp(p1.name, p2.name))

print L2[0].name
print L2[1].name
print L2[2].name
