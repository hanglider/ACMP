n = int(input())
d = [1]
for i in range(1, n + 1):
    d += [d[-1] + (i % 2 < 1) * d[i // 2]]
print(d[n])
