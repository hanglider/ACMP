s = [*map(int, open(0).read().split())]
k = 1
for _ in range(s[0]):
    n, m = s[k:k + 2]
    a = s[k + 2:]
    k += 2 + n * m
    print("YNEOS"[any(a[i] == a[i + 1] == a[i + m] == a[i + m + 1] for i in range(n * m - m) if (i + 1) % m)::2])
