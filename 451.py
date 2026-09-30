import re
from math import *
p = ' '
r = ''
for x in re.findall(r'\d+\.?\d*(?:e[+-]?\d+)?|[a-z]+|\S', input().lower()):
    if x in '+-*/' and p[-1] not in ')0123456789.' or p in ('sin', 'cos') and x != '(' or x not in ('sin', 'cos', '(', ')', '+', '-', '*', '/') and not x[0].isdigit():
        x = '@'
    elif x[0].isdigit():
        x = str(float(x))
    r += x + ' '
    p = x
try:
    print('%f' % eval(r))
except:
    print('Error')
