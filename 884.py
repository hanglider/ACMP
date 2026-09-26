k = int(input())
s = input().strip()
c = [0] * 26
m = 0
W = set()
for i in range(len(s)):
    x = ord(s[i]) - 65
    c[x] += 1
    m |= 1 << x
    if i >= k:
        y = ord(s[i - k]) - 65
        c[y] -= 1
        if not c[y]:
            m ^= 1 << y
    if i >= k - 1:
        W.add(m)
Z = [int(('0' * (1 << j) + '1' * (1 << j)) * (4096 >> j), 2) for j in range(13)]
P = [0] * 14
for y in range(8192):
    P[bin(y).count('1')] |= 1 << y
b = -1
for T in range(8):
    F = [0] * 1024
    for w in W:
        if w >> 23 & ~T == 0:
            F[w >> 13 & 1023] |= 1 << (w & 8191)
    for j in range(10):
        for x in range(1024):
            if x >> j & 1:
                F[x] |= F[x ^ 1 << j]
    for x in range(1024):
        B = F[x]
        for j in range(13):
            B |= (B & Z[j]) << (1 << j)
        h = bin(T).count('1') + bin(x).count('1')
        for t in range(13, -1, -1):
            g = P[t] & ~B
            if h + t <= b:
                break
            if g:
                b = h + t
                R = T << 23 | x << 13 | (g & -g).bit_length() - 1
                break
L = sorted(a for a in set(s) if not R >> ord(a) - 65 & 1)
print(len(L))
print(*L, sep='\n')