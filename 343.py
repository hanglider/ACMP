n, m, k, *a = map(int, open(0).read().split())
s = set()
for t, y, x in zip(*[iter(a)] * 3):
    c = {(y + i // 2, x + i % 2) for i in range(4) if i != t - 1}
    if 0 < y < n and 0 < x < m and not c & s:
        s |= c
print(len(s))
