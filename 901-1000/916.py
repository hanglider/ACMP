n, k, *c = map(int, open(0).read().split())
print(sum((i // k + 1) * x for i, x in enumerate(sorted(c)[::-1])))
