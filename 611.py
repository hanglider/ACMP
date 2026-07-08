from itertools import combinations

def S(l):
    m = len(l)
    u = [False] * m
    r = []
    def b(k):
        if k == m:
            for c in range(m):
                s = ''.join(r[t][c] for t in range(m))
                if s not in l:
                    return False
            return True
        for i in range(m):
            if not u[i]:
                w = l[i]
                o = True
                for c in range(m):
                    p = ''.join(r[t][c] for t in range(k)) + w[c]
                    if not any(x.startswith(p) for x in l):
                        o = False
                        break
                if o:
                    u[i] = True
                    r.append(w)
                    if b(k + 1):
                        return True
                    r.pop()
                    u[i] = False
        return False
    return list(r) if b(0) else None

n = int(input())
W = [input() for _ in range(2 * n)]
m = 2 * n
k = n
A = B = None
for c in combinations(range(1, m), k - 1):
    g = [W[0]] + [W[i] for i in c]
    h = [W[i] for i in range(1, m) if i not in c]
    gA = S(g)
    if gA:
        gB = S(h)
        if gB:
            A, B = gA, gB
            break
print('\n'.join(A))
print()
print('\n'.join(B))
