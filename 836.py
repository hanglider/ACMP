n, *a = map(int, open(0).read().split())
s = sorted(x for x in a if x & 65 == 64)
print(len(s))
print(*s)
