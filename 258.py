k, m, l, p, n = map(int, input().split())
a = set()
b = set()
for f in range(1, 1002):
    e = (l - 1) // f
    if e // m + 1 == p and e % m + 1 == n:
        e = (k - 1) // f
        a.add(e // m + 1)
        b.add(e % m + 1)
if a:
    print((len(a) < 2) * a.pop(), (len(b) < 2) * b.pop())
else:
    print(-1, -1)
