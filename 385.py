n, *a = map(int, open(0).read().split())
p = list(zip(a[::2], a[1::2]))
s = sorted({(x - u)**2 + (y - v)**2 for i, (x, y) in enumerate(p) for u, v in p[:i]})
print(len(s))
for x in s:
    print(x**.5)
