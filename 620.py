t = iter(map(float, open(0).read().split()))
n = int(next(t))
R = [[(next(t), next(t)) for _ in range(int(next(t)))] for _ in range(n)]
m = 0
for i in range(n):
    s = {i}
    for _ in R:
        s |= {j for j in range(n) if R[j][-1] in sum([R[k][:-1] for k in s], [])}
    P = sorted(set(sum([R[k] for k in s], [])))
    H = []
    for p in P + P[::-1]:
        while len(H) > 1 and (H[-1][0] - H[-2][0]) * (p[1] - H[-2][1]) < (H[-1][1] - H[-2][1]) * (p[0] - H[-2][0]):
            H.pop()
        H.append(p)
    m = max(m, abs(sum(a * d - b * c for (a, b), (c, d) in zip(H, H[1:]))))
print('%.2f' % (m / 2))
