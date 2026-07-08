I = input
n, m, k= map(int, I().split())
g = [I() for _ in range(n)]
D = [0] *(1 << m)
D[0] = 1
for r in g:
    E = D[:]
    for s in range(1 << m):
        for j in range(m):
            if s >> j & 1 == 0 < (r[j] == 'Y'):
                E[s|1 << j] += D[s]
    D = E
print(sum(D[s] for s in range(1 << m) if bin(s).count('1') == k))
