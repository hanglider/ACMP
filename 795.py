n, *s = map(int, open(0).read().split())
a, b, k = s[n:]
l = (a - 1) // k
print(max(max(s[c % n], s[-c % n]) for c in range(l, min((b - 1) // k, l + n) + 1)))
