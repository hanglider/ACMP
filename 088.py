n, *a = map(int, open(0).read().split())
k = n * n
d = {x for i, v in enumerate(a) for x in ((i // k, v), (i % k, v, 0), (i // k // n, i % k // n, v))}
print(["Inc", "C"][len(d) == 3 * len(a) and 0 < min(a) <= max(a) <= k] + "orrect")
