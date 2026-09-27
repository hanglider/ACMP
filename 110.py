n, k = map(int, input().split())
a = str(n // k)
f = str(n % k * 10**9 // k).zfill(9)
o = []
for i in range(1, int(max(a + f)) + 1):
    A, F, C = ["".join(str(k * (c >= str(i))) for c in x) for x in (a, f[:3], f[3:])]
    C = C[:min(p for p in range(1, 7) if C[:p] * (6 // p) == C)]
    while F and F[-1] == C[-1]:
        F = F[:-1]
        C = C[-1] + C[:-1]
    o += [(A.lstrip("0") or "0") + "." * (F + C > "0") + F + ("(" + C + ")") * (C > "0")]
print(n, "+".join(o), sep="=")
