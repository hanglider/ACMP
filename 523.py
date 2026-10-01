n, *a, k = map(int, open(0).read().split())
l = max(a)
h = sum(a)
while l < h:
    m = (l + h) // 2
    c = 1
    s = 0
    for x in a:
        s += x
        if s > m:
            c += 1
            s = x
    if c > k:
        l = m + 1
    else:
        h = m
print(l)
