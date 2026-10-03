n, l = map(int, input().split())
b = [input() for _ in range(n)]
s = input()
m = len(s)
w = l + 1
t = '#'.join(b)
g = {h: int(''.join('01'[z == h] for z in t)[::-1], 2) for h in s}
for k in range(1, m + 1):
    R = []
    c = []
    for j in range(k):
        q = -1
        for i, h in enumerate(s[j::k]):
            q &= g[h] >> i
        R.append(q)
        z = 1
        while z < n:
            q |= q >> z * w
            z *= 2
        c.append(q & (1 << l) - 1)
    P = [-1]
    for q in c:
        P.append(P[-1] & q)
    S = [-1]
    for q in c[::-1]:
        S.append(S[-1] & q)
    for r in range(k):
        v = P[k - r] & S[r] >> 1
        if v:
            c = (v & -v).bit_length() - 1
            a = [0] * k
            for j in range(k):
                a[(r + j) % k] = next(i + 1 for i in range(n) if R[j] >> i * w + c + (r + j) // k & 1)
            print(k)
            print(*a)
            exit()
print(-1)
