a = list(map(int, open(0).read().split()))
p = q = r = 1
for i in range(3):
    b, c = sorted(a[i:6:3]), sorted(a[i + 6::3])
    p *= b[1] - b[0]
    q *= c[1] - c[0]
    r *= max(0, min(b[1], c[1]) - max(b[0], c[0]))
print(p + q - r)
