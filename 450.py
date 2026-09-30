from itertools import *
n, *a = map(int, open(0).read().split())
s, p = max((sum(a[i * n + j] for i, j in enumerate(p)), p) for p in permutations(range(n)))
print(''.join(chr(65 + j) for j in p))
print(sum(a) - s)
