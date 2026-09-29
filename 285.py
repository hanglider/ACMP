n, m, *a = map(int, open(0).read().split())
print("yneos"[not max(a) <= m <= sum(a) - n + 1::2])
