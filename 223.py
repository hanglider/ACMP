import sys
from functools import lru_cache as r
sys.setrecursionlimit(10**6)
a = input()
b = input()
@r(maxsize=None)
def f(i,j,L):
    if L == 0:
        return 1
    r = 0
    for k in range(L):
        if a[i] == b[j + k]:
            r += f(i + 1, j, k) * f(i + k + 1, j + k + 1, L - 1 - k)
    return r

print(f(0, 0, len(a)))
