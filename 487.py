n, k, p, *a = map(int, open(0).read().split())
for x in a:
    print("FT"[n % (k + 1) < 1 or (n - x) % (k + 1) < 1])
    n -= x
