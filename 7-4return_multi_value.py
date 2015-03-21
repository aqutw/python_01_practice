import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = r = move(100, 100, 60, math.pi/6)
print r
print x, y

print '--------do Task---------'
def quadratic_equation(a, b, c):
    t = math.sqrt(b*b - 4*a*c)
    return (-b+t) / (2*a), (-b-t) / (2*a)

print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)
