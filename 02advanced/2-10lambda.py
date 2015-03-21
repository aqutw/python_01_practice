# -*- coding: utf-8 -*-
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
#匿名函数只能有一个表达式，不写return，返回值就是该表达式的结果。


print sorted([1, 3, 9, 5, 0], lambda x,y: -cmp(x,y))



myabs = lambda x: -x if x < 0 else x 
print myabs(-5)
print myabs(5)



print filter(lambda s: s and len(s.strip())>0, ['test', None, '', 'str', ' ', 'END'] )
#                     ^^^ for None
