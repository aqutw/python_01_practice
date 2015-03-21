def int2(x, base=2):
    return int(x, base)

print int2('10')
print int2('111')

###

import functools
int2 = functools.partial(int, base=2)
print int2('1000000')
print int2('1010101')

###
print '--do Task--'

"""
def reversed_cmp_str(x, y): #copy from 2-7
  x = x.lower()
  y = y.lower()
  if x>y: return 1
  if x<y: return -1
  return 0

sorted_ignore_case = functools.partial()
"""

print '#official answer'
import functools
sorted_ignore_case = functools.partial(  sorted, cmp=lambda s1, s2: cmp(s1.upper(), s2.upper())  ) #see cpm=
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])


print cmp('A','B') # -1
print cmp('A','a') # -1
