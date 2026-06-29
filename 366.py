d = open('input.txt').read().split()
N, S = map(int, d[:2])
X = list(map(int, d[2:N+2]))
n = N // 2

L = {X[0]: 0}
for v in X[1:n]:
    L = {s + b * v: (m << 1) | (b < 0) for s, m in L.items() for b in (1, -1)}

R = {0: 0}
for v in X[n:]:
    R = {s + b * v: (m << 1) | (b < 0) for s, m in R.items() for b in (1, -1)}

for r, rm in R.items():
    if S - r in L:
        lm = L[S - r]
        a = str(X[0])
        for i, v in enumerate(X[1:n]):
            a += "+-"[lm >> (n - 2 - i) & 1] + str(v)
        for i, v in enumerate(X[n:]):
            a += "+-"[rm >> (N - n - 1 - i) & 1] + str(v)
        print(f"{a}={S}")
        exit()

print("No solution")
