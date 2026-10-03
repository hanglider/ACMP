from array import array
def f():
    I = open(0)
    n, m = map(int, I.readline().split())
    U = array('i')
    V = array('i')
    for x in I:
        u, v = x.split()
        U.append(int(u))
        V.append(int(v))
    X = array('i', map(int.__xor__, U, V))
    s = array('i', [0]) * (n + 2)
    for v in U:
        s[v + 1] += 1
    for v in V:
        s[v + 1] += 1
    for v in range(1, n + 2):
        s[v] += s[v - 1]
    g = array('i', s)
    a = array('i', [0]) * (2 * m)
    for e in range(m):
        u = U[e]
        a[g[u]] = e
        g[u] += 1
        u = V[e]
        a[g[u]] = e
        g[u] += 1
    J = list(map(range, s, s[1:]))
    t = array('i', [0]) * (n + 1)
    l = array('i', t)
    p = array('i', [-1]) * (n + 1)
    q = array('i', t)
    C = array('i', [0]) * m
    k = 1
    r = 1
    E = array('i')
    for z in range(1, n + 1):
        if t[z]:
            continue
        t[z] = l[z] = k
        k += 1
        J[z] = iter(J[z])
        S = [z]
        while S:
            v = S[-1]
            h = t[v]
            for i in J[v]:
                e = a[i]
                w = X[e] ^ v
                y = t[w]
                if not y:
                    break
                if y < h and e != p[v]:
                    E.append(e)
                    if y < l[v]:
                        l[v] = y
            else:
                S.pop()
                if S:
                    u = S[-1]
                    if l[v] < l[u]:
                        l[u] = l[v]
                    if l[v] >= t[u]:
                        b = E[q[v]:]
                        del E[q[v]:]
                        for c, e in enumerate(b, 1):
                            C[e] = c
                        if len(b) > r:
                            r = len(b)
                continue
            p[w] = e
            q[w] = len(E)
            t[w] = l[w] = k
            k += 1
            J[w] = iter(J[w])
            E.append(e)
            S.append(w)
    print(r)
    for i in range(0, m, 5000):
        print('\n'.join(f'{U[e]} {V[e]} {C[e]}' for e in range(i, min(i + 5000, m))))
f()
