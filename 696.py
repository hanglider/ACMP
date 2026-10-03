r, c, *p = open(0).read().split()
c = int(c)
s = ''.join(p[4:])
b = 1e9
for m in range(16):
    d = 'X' + ''.join(x for i, x in enumerate('RGBY') if m >> i & 1 < 1)
    v = {s.find('S')}
    q = list(v)
    for i in q:
        for j in i - 1, i + 1, i - c, i + c:
            if 0 <= j < len(s) and (j % c == i % c or j // c == i // c) and j not in v and s[j] not in d:
                v.add(j)
                q += [j]
    if s.find('E') in v:
        b = min(b, sum(int(p[i]) for i in range(4) if m >> i & 1))
print(b if b < 1e9 else 'Sleep')
