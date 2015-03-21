# -*- coding: utf-8 -*-
def fn(*args):
    print args
    return args

print fn(1,2)
print fn(1,2,) #one more a dot is OK
print fn(1,2,3)
print fn(1,2,3,4) #return a tuple? Yes. (remeber you should return args.)

(a,b,c,d) = fn('1','2','3','4') #CANNOT use (a,b,c)
print a
print b
print c

print '----do Task------'

def my_avg(*args):
    total = 0
    n = 0 #...or use len(args)
    for v in args:
        n+=1 #Can't I use n++???? #python不支持c语言中的自增1（++）或1（--）运算符，因为+和-也是单目运算符，python将++n解释为n，将--n解释为-（-n），从而得到n FROM http://f.dataguru.cn/thread-78327-1-1.html
        total+=v
    return total/n if n>0 else 0

print my_avg(1,2,3)
print my_avg(5,5,5,5,5,5,)
print my_avg()
