from array import *
n, m, k = map(int, input().split())
c = dict(zip(sorted(range(1, k + 1), key=str), map(array, 'H' * k, zip(*[array('H', sorted(range(k), key=input().split().__getitem__)) for _ in range(n)]))))
r = k
for i in range(k - 1, 0, -1):
    if sum(map(int.__lt__, c[i], c[r])) >= m:
        r = i
print(r)
