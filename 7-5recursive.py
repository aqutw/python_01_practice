# -*- coding: utf-8 -*-
def fact(n):
    if n==1:
        return 1
    return fact(n-1) * n


print fact(3)


print '-----do Task-----'

#汉诺塔
def move(n, a, b, c): 
    if n==1:
        print a, '-->', c
        return
    move(n-1, a, c, b)
    print a, '-->', c
    move(n-1, b, a, c)
move(4, 'A', 'B', 'C')
