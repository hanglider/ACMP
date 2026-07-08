import heapq
H = heapq.heappush
y = heapq.heapreplace
O = heapq.heappop

D = list(map(int, open('input.txt').read().split()))
n = D[0]
m = D[1]
K = D[2]
g = [[] for _ in range(n + 1)]
v = 3
for e in range(1, m + 1):
    a = D[v]
    b = D[v + 1]
    c = D[v + 2]
    v += 3
    g[a].append((b, c, e))
    g[b].append((a, c, e))

L = [[] for _ in range(n + 1)]
for x in range(1, n + 1):
    if len(g[x]) == 1:
        u, c, e = g[x][0]
        L[u].append((c, e))

S = [x for x in range(1, n + 1) if len(g[x]) > 1]
N = {x: [t for t in g[x] if len(g[t[0]]) > 1] for x in S}
E = [x for x in S if len(N[x]) < 2]
Y = not E
T = E[0] if E else S[0]
q = [T]
C = []
I = []
Z = 0
U = T
while 1:
    X = 0
    for u, c, e in N[U]:
        if u != Z:
            X = (u, c, e)
            break
    if not X:
        break
    u, c, e = X
    C.append(c)
    I.append(e)
    if u == T:
        break
    q.append(u)
    Z = U
    U = u

p = len(q)
l = [sorted([c for c, e in L[x]]) for x in q]
M = l + l if Y else l
W = C + C if Y else C
P = [0]
for w in W:
    P.append(P[-1] + w)

V = -1
f = s = F = 0

for i in range(p):
    Q = []
    d = 0
    h = min(i + K, i + p - 1 if Y else p - 1)
    k = P[i]
    for j in range(i, h + 1):
        r = K - j + i
        if len(Q) > r:
            d += Q[0]
            O(Q)
        for c in M[j]:
            if len(Q) < r:
                H(Q, -c)
                d += c
            elif Q and c < -Q[0]:
                d += c + Q[0]
                y(Q, -c)
            else:
                break
        if len(Q) == r:
            t = P[j] - k + d
            if V < 0 or t < V:
                V = t
                f = i
                s = j

if Y and K >= p:
    A = sorted(c for x in q for c, e in L[x])
    if K - p <= len(A):
        t = P[p] + sum(A[:K - p])
        if V < 0 or t < V:
            V = t
            F = 1

if F:
    A = sorted((c, e) for x in q for c, e in L[x])
    R = I + [e for c, e in A[:K - p]]
else:
    A = sorted((c, e) for t in range(f, s + 1) for c, e in L[q[t % p]])
    R = (I + I)[f:s] + [e for c, e in A[:K - s + f]]

print(*R, sep='\n')
