r, c = map(int, open('INPUT.TXT').read().split())
if r < c:
    r, c = c, r
w = c
p = [3**k for k in range(w + 2)]
D = {0: 1}
z = 0
for i in range(r):
    for j in range(w):
        a = p[j]
        b = p[j + 1]
        E = {}
        g = E.get
        for s, v in D.items():
            L = s // a % 3
            U = s // b % 3
            t = s - L * a - U * b
            if L == 0:
                if U == 0:
                    n = t + a + 2 * b
                    E[n] = g(n, 0) + v
                else:
                    n = t + U * a
                    E[n] = g(n, 0) + v
                    n = t + U * b
                    E[n] = g(n, 0) + v
            elif U == 0:
                n = t + L * a
                E[n] = g(n, 0) + v
                n = t + L * b
                E[n] = g(n, 0) + v
            elif L == 1:
                if U == 1:
                    k = j + 2
                    d = 1
                    while 1:
                        x = t // p[k] % 3
                        if x == 1:
                            d += 1
                        if x == 2:
                            d -= 1
                            if d == 0:
                                break
                        k += 1
                    n = t - p[k]
                    E[n] = g(n, 0) + v
                elif t == 0 and i == r - 1 and j == w - 1:
                    z += v
            elif U == 1:
                E[t] = g(t, 0) + v
            else:
                k = j - 1
                d = 1
                while 1:
                    x = t // p[k] % 3
                    if x == 2:
                        d += 1
                    if x == 1:
                        d -= 1
                        if d == 0:
                            break
                    k -= 1
                n = t + p[k]
                E[n] = g(n, 0) + v
        D = E
    if i < r - 1:
        D = {s * 3: v for s, v in D.items() if s < p[w]}
print(z)
