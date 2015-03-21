L = ['Adam', 'Lisa', 'Bart', 'Paul']

L2 = L[0:3]
L3 = L[:3] #the result is same above
L4 = L[1:3]
L_copied = L[:] #copy/clone!

L5 = L[::2]

print '--test--'
print L
print L2
print L3
print L4
print L_copied
print L5

print '--do Task--'
a = range(1, 101)
print a[:10]
print a[2::3] # 3 6 9 12 ~ 99
print a[4:50:5] # 5 10 15 20 ~ 50
