from math import factorial as f
g = lambda n, k: f(n) // (f(k)*f(n-k))
n = int(input())
t = r = 0
for i in range(2, -1, -1):
    p = i
    while t < n:
        t += g(p, i)
        p += 1
    p -= 1
    t -= g(p, i)
    r += 2**p
print(r)