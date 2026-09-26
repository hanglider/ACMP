t = input().split()
n = int(t[0])
c = [*range(n + 1)]
f = [-1] * (n + 1)
S = {j: [j] for j in c}
for w in t[2:]:
    i = int(w[:-1])
    b = c[i]
    Y = max(c[i - 1], b)
    s = f[i - 1] * ((w[-1] > 'F') * 2 - 1)
    U = []
    for k, L in S.items():
        m = [x for x in L if x >= i]
        if m:
            d = s if (k >= Y) == (b >= Y) else -s
            if (L[-len(m):] if d > 0 else L[:len(m)]) != m:
                print('SCRUFFY')
                exit()
            S[k] = [x for x in L if x < i]
            U += (2 * Y - 1 - k, d, m[::-1]),
    for k, d, m in U:
        L = S.get(k, [])
        S[k] = L + m if d > 0 else m + L
        for x in m:
            c[x] = k
            f[x] = -f[x]
A = []
B = []
for L in S.values():
    if L:
        (A if f[L[0]] < 0 else B).append(L[0])
        (A if f[L[-1]] > 0 else B).append(L[-1])
print(*['P%dF' % x for x in sorted(A)] + ['P%dR' % x for x in sorted(B)])