n, *a = map(int, open(0).read().split())
i = s = 0
for t in range(10):
    k = 1 + (a[i] < 10)
    s += sum(a[i:i + 2 + (sum(a[i:i + k]) > 9)])
    i += k
print(s)
