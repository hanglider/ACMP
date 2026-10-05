k, m, *a = map(int, open(0).read().split())
for h, p in sorted(zip(a[1::2], a[::2]))[::-1]:
    if p == k:
        k += 1
    elif p + 1 == k:
        k -= 1
print(k)
