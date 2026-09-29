n, *a = map(int, open(0).read().split())
t = [a[i] * a[n + i] for i in range(n)]
print(t.index(max(t)) + 1)
