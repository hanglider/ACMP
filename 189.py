from math import factorial as f
n, k = map(int, open(0).read().split())
k -= 1
s = [*range(1, n + 1)]
r = []
for i in range(n - 1, -1, -1):
    r += [s.pop(k // f(i))]
    k %= f(i)
print(*r)
