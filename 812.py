n, a = map(int, input().split())
d = [0] * a + [1]
s = 1
for _ in range(n):
    d += [s]
    s += s - d[-a - 1]
print(d[-1])
