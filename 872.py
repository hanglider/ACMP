m, *s = open(0).read().split()
s = set(s)
print(max(sum(w.startswith(u) for u in s) for w in s))
