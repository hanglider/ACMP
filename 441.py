from bisect import *
n = int(input())
a = input().split()
b = input().split()
i = sorted(range(n), key=a.__getitem__)
j = sorted(range(n), key=b.__getitem__)
if any(a[x] != b[y] for x, y in zip(i, j)):
    print(-1)
else:
    s = [[y] for _, y in sorted(zip(i, j))]
    r = 0
    while s[1:]:
        r += sum(len(x) * len(y) - sum(map(bisect, [x] * len(y), y)) for x, y in zip(s[::2], s[1::2]))
        s = [sorted(x + y) for x, y in zip(s[::2], s[1::2])] + s[len(s) & ~1:]
    print(r)
