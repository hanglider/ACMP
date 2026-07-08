n, m = map(int, input().split())
v = list(map(int, input().split()))
p = list(range(n))
def f(x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ra = f(a)
    rb = f(b)
    if ra != rb:
        w = max(ra, rb)
        l = min(ra, rb)
        v[w] += v[l]
        v[l] = 0
        p[l] = w
for i in range(n):
    if v[i] > 0:
        print(i + 1, v[i])
