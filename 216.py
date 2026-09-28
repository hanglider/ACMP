n, *k = map(int, open(0).read().split())
s = sum(k)
print(min(s // 2, s - max(k)))
