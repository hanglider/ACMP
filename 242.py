a = open(0).read().split()
n = int(a[0])
b = [a[2 + i * n:2 + i * n + n] for i in range(n)]
p = lambda x: bin(x).count('1')
r = [9**9, 0]
for g in b, list(zip(*b)):
    P = {}
    Q = {}
    for i in range(n):
        for j in range(n):
            c = g[i][j]
            P.setdefault(c, [0] * n)[j] |= 1 << i
            Q.setdefault(c, [0] * n)[i] += 1
    for c in P:
        s = sum(1 << i for i in range(n) if Q[c][i] > 1)
        o = sum(1 << i for i in range(n) if Q[c][i] == 1)
        l = P[c]
        for k, e in (0, p(s) == n), (1, min(Q[c]) and any(p(s | x) > 1 and x & o < 1 for x in l)), (2, any(p(s | x) > 1 and p(s | o & ~x) > 1 for x in l)):
            if e:
                r = min(r, [n + k, int(c)])
                break
print(*r if r[1] else (0, 0))
