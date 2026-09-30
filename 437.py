from array import array
from bisect import bisect_left as f
from itertools import accumulate
import re
k, n, m = map(int, input().split())
X = array('q')
Y = array('q')
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
U = array('q')
for y in sorted(Y):
    if not U or U[-1] < y:
        U.append(y)
u = len(U)
A = bytearray(u + 1)
U.append(0)
G = [array('i') for _ in range(18)]
P = array('i', (f(U, x, 0, u) for x in X))
Q = array('i', (f(U, y, 0, u) for y in Y))
for i in range(n):
    if U[P[i]] != X[i]:
        P[i] = u
    j = ((X[i] - 1) ^ (Y[i] - 1)).bit_length() - 1
    if j < 18:
        G[j].append(i)
del X, Y
for j in range(min(k - 1, 18)):
    if G[j]:
        C = array('i', [0]) * u
        for i in G[j]:
            C[Q[i]] += A[P[i]] == 0
        D = array('i', accumulate(map(bool, A), initial=0))
        E = bytearray(u + 1)
        for i in G[j]:
            q = Q[i]
            b = ((U[q] - 1) >> j ^ 1) << j
            if A[q] == 0 and 2**j - D[f(U, b + 2**j + 1, 0, u)] + D[f(U, b + 1, 0, u)] == C[q]:
                E[q] = j + 1
        A = bytearray(map(max, A, E))
print(*[A[i] if (i := f(U, int(z[0]), 0, u)) < u and U[i] == int(z[0]) and A[i] else k for z in re.finditer(r'\d+', input())])
