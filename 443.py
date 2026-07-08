d = open('input.txt', 'rb').read().split()
n, m, x = int(d[0]), int(d[1]), int(d[2])
p = [1] * 105
for i in range(1, 105):
    p[i] = p[i-1] * x % m
c = [0] * m
for s in d[3:]:
    c[sum((b - 48) * w for b, w in zip(s, p)) % m] += 1
print(sum(v * (v - 1) for v in c) // 2)
