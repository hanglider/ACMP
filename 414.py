n, a, b, *p = map(int, open(0).read().split())
p = [0, 0] + p
while a != b:
    if a > b:
        a = p[a]
    else:
        b = p[b]
print(a)
