n, s, k, *q = open(0).read().split()
r = ''
for m in q:
    h = 2**int(n)
    j = h - int(m)
    f = 0
    for c in s:
        h //= 2
        if j == h:
            r += 'OK'[(c == 'Z') ^ f]
        if j > h:
            j = 2 * h - j
            f ^= 1
print(r)
