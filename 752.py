l, r = map(int, input().split())
f = [0, 1] + [0] * 2 * l
c = [1]
for k in range(1, l // 2 + 1):
    c = [(a + b) % r for a, b in zip([0] + c, c + [0])]
    f[2 * k:3 * k + 1] = [(a + f[k] * b) % r for a, b in zip(f[2 * k:3 * k + 1], c)]
print(f[l] % r)
