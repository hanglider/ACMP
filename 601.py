import sys
from array import*
n, m = map(int, input().split())
a = array('h', [0]) * 101 * (n + 1)
for _ in range(m):
    u, v, c = map(int, input().split())
    a[u * 101 + c] = v
    a[v * 101 + c] = u
r = 1
for c in sys.stdin.read().split()[1:]:
    r = a[r * 101 + int(c)]
print(r or 'INCORRECT')
