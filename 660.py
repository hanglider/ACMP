from bisect import bisect_right as b
n, m, k, *a = map(int, open(0).read().split())
L = [c - (c & -c) for c in range(m + 2)]
R = [min(c + (c & -c), m + 1) for c in range(m + 2)]
l = [0] * (m + 2)
g = [[] for _ in range(n + 2)]
for i in range(0, 2 * k, 2):
    g[a[i]].append(a[i + 1])
z = s = j = y = 0
for t in range(1, n + 1):
    if g[t]:
        q = [0] + sorted(g[t]) + [m + 1]
        h = len(q) - 1
        y += h
        for i in range(1, h):
            c = q[i]
            d = L[c]
            while d > q[i - 1]:
                z += l[d] * (d - L[d]) * (c - R[d])
                R[d] = c
                d = L[d]
                j += 1
            d = R[c]
            while d < q[i + 1]:
                z += l[d] * (R[d] - d) * (L[d] - c)
                L[d] = c
                d = R[d]
                j += 1
            z -= l[c] * (c - L[c]) * (R[c] - c)
        for i in range(1, h):
            c = q[i]
            L[c] = q[i - (i & -i)]
            R[c] = q[min(i + (i & -i), h)]
            z += t * (c - L[c]) * (R[c] - c)
            l[c] = t
    s += z
    if j > 30 * y + 99999:
        break
else:
    print(m * (m + 1) * n * (n + 1) // 4 - s)
    exit()
y = t + 1
e = sorted((l[c], y, c) for c in range(1, m + 1) if l[c])
e += [(t, t, c) for t in range(y, n + 1) for c in g[t]]
w = s
z = [(1, m, e)]
while z:
    l, h, e = z.pop()
    if not e:
        continue
    if l == h:
        p = 0
        q = y
        for t, x, c in e:
            w += p * (x - q)
            p = t
            q = x
        w += p * (n + 1 - q)
        continue
    o = (l + h) // 2
    z += [(l, o, [x for x in e if x[2] <= o]), (o + 1, h, [x for x in e if x[2] > o])]
    u = o - l + 1
    r = h - o
    A = [-1, -1, 0]
    B = [-5, 0, u]
    C = [0, 0, 0]
    D = [-1, -1, 0]
    E = [-5, 0, r]
    F = [0, 0, 0]
    v = 0
    q = y
    for t, x, c in e:
        w += v * (x - q)
        q = x
        d = 0
        if c <= o:
            s = o - c
            while B[-2] >= s:
                f = A.pop()
                i = b(D, f)
                d += (B.pop() - B[-1]) * (f * E[i - 1] + F[-1] - F[i - 1])
                C.pop()
            g = B[-1] - s
            if g > 0:
                f = A[-1]
                i = b(D, f)
                d += g * (f * E[i - 1] + F[-1] - F[i - 1])
                B[-1] = s
                C[-1] -= g * f
            g = u - s
            A.append(t)
            B.append(u)
            C.append(C[-1] + g * t)
            v += g * r * t - d
        else:
            s = c - o - 1
            while E[-2] >= s:
                f = D.pop()
                i = b(A, f)
                d += (E.pop() - E[-1]) * (f * B[i - 1] + C[-1] - C[i - 1])
                F.pop()
            g = E[-1] - s
            if g > 0:
                f = D[-1]
                i = b(A, f)
                d += g * (f * B[i - 1] + C[-1] - C[i - 1])
                E[-1] = s
                F[-1] -= g * f
            g = r - s
            D.append(t)
            E.append(r)
            F.append(F[-1] + g * t)
            v += g * u * t - d
    w += v * (n + 1 - q)
print(m * (m + 1) * n * (n + 1) // 4 - w)
