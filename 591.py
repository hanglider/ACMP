r = list(map(int, open(0).read().split()))
n, m = r[:2]
a = r[2::3]
b = r[3::3]
c = r[4::3]
def f(x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x
def g(l, k):
    global p
    p = list(range(n + 1))
    t = []
    for i in l:
        x = f(a[i])
        y = f(b[i])
        if x != y and (c[i] < 2 or k):
            p[x] = y
            t += [i]
            k -= c[i] - 1
    return t, k
s = sorted(range(m), key=c.__getitem__)
t, _ = g(s, m)
t = [i for i in t if c[i] > 1]
t, k = g(t + s[::-1], len(t) + len(t) % 2)
print(*k and [-1] or sorted(i + 1 for i in t), sep='\n')
