n = int(input())
P = ''.join(k[0] * (k.index(c) + 1) for c in input().strip() for k in 'ABC DEF GHI JKL MNO PQRS TUV WXYZ'.split() if c in k)
m = len(P)
d = [[0] * (n + 1) for _ in range(m + 1)]
d[0][0] = 1
for i in range(m):
    for l in range(1, 4 + (P[i] in 'PW')):
        if P[i:i + l] == P[i] * l:
            for j in range(n):
                d[i + l][j + 1] += d[i][j]
print(d[m][n])