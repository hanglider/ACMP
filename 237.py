n, m, *a = open(0).read().split()
s = sorted("".join(a[:int(n)]))
for c in "".join(a[int(n):]):
    s.remove(c)
print("".join(s))
