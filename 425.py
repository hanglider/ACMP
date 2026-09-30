n, w, e = map(int, input().split())
m = 100 * n
print(sum(k <= max(a, a + e - w) and min(a, a + e - w) <= k + m for i in range(n) for a in [w * n + (e - w) * i] for k in range(0, m * n, m)))
