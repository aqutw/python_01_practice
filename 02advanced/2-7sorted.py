a = sorted([36, 5, 12, 9, 21])
print a

def reversed_cmp(x, y):
  if x>y: return -1
  if x<y: return 1
  return 0

print sorted([36,5,12,9,21], reversed_cmp)




def reversed_cmp_str(x, y):
  x = x.lower()
  y = y.lower()
  if x>y: return 1
  if x<y: return -1
  return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], reversed_cmp_str)
