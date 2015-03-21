# -*- coding: utf-8 -*-

#注意: 观察 for 循环在遍历set时，元素的顺序和list的顺序很可能是不同的，而且不同的机器上运行的结果也可能不同。

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)]

for v in s:
    print v[0]+':', v[1]
