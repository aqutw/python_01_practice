# -*- coding: utf-8 -*-

#set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。

#set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。

#最后，set存储的元素也是没有顺序的。

months = set(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
x1 = 'Feb'
x2 = 'Sun'

if x1 in months:
    print 'x1: ok'
else:
    print 'x1: error'

if x2 in months:
    print 'x2: ok'
else:
    print 'x2: error'
