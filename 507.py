n, *a = map(int, open(0).read().split())
b = a[n:]
r = range(n)
v = set()
t = []


def g(s):
    if s in v:
        return
    v.add(s)
    m = 1
    for i in r:
        for j in r:
            if b[i * n + j] and s[i] and s[j] > (i == j):
                g(s[:j] + (s[j] - 1,) + s[j + 1:])
                m = 0
    if m:
        t.append(s)


g(tuple(a[:n]))
print(len(t))
for s in t:
    print(*s)
