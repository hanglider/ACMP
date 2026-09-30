k, *a = map(int, open(0).read().split())
print(sum(x // 2 + 1 for x in sorted(a)[:k // 2 + 1]))
