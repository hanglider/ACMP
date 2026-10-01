n, m = map(int, input().split())
c = [0] * 10
for i in range(1, n + 1):
    s = str([*range(i, i * m + 1, i)])
    for d in range(10):
        c[d] += s.count(str(d))
print(*c, sep="\n")
