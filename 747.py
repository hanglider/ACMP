s = input().strip()
n = len(s)
h = n // 2
b = [int(''.join(str(+(x == c)) for x in s), 2) for c in set(s)]
E = [0] + [0] * h
for p in range(1, h + 1):
    for x in b:
        E[p] |= x & x << p


def R(x, l):
    k = 1
    while 2 * k <= l:
        x &= x << k
        k *= 2
    return x & x << l - k


T = [[] for _ in range(n)]
for p in range(1, h + 1):
    m = R(E[p], p)
    q = p
    d = 2
    while d <= q:
        if q % d < 1:
            m &= ~R(E[p // d], 2 * p - p // d)
            while q % d < 1:
                q //= d
        d += 1
    f = format(m, '0%db' % n)
    j = f.find('1')
    while j >= 0:
        T[j].append(p)
        j = f.find('1', j + 1)
I = 10**9
d = [0] + [I] * n
m = I
z = {}
for j in range(n):
    d[j] = min(d[j], j + m)
    m = min(m, d[j] - j)
    for p in T[j]:
        v, l = z.get((p, j % p), (I, 0))
        v = min(v if l == j - p else I, d[j])
        z[p, j % p] = v, j
        d[j + 2 * p] = min(d[j + 2 * p], v + p)
d[n] = min(d[n], n + m)
i = n
r = []
while i:
    j = i - 1
    while 1:
        c = d[i] - d[j]
        if c == i - j:
            r += [s[j:i] + ' 1']
            break
        if c > 0 and (i - j) % c < 1 and s[j:i] == s[j:j + c] * ((i - j) // c):
            r += [s[j:j + c] + ' %d' % ((i - j) // c)]
            break
        j -= 1
    i = j
print(d[n])
print('\n'.join(r[::-1]))
