p = k = 0
d = 1
v = {0}
for c in input():
    if c == 'S':
        p += d
        k += 1
        if p in v:
            print(k)
            exit()
        v.add(p)
    else:
        d *= 1j - 2j * (c > 'L')
print(-1)
