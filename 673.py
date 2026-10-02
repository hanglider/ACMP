from itertools import *
from math import *
n = int(input())
c = 0
m = []
for k in range(min(n, 7) + 1):
    for d in combinations_with_replacement(range(2, 10), k):
        if sum(d) + n - k == prod(d):
            c += perm(n, k) // prod(factorial(d.count(x)) for x in set(d))
            m += [int('1' * (n - k) + ''.join(map(str, d)))]
print(*[c, min(m)] if n > 1 else [10, 0])
