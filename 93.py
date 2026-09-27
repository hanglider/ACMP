t = open(0).read().split()
n = int(t[0])
print(*[sum(len(g) == len(w) and sum(a != b for a, b in zip(g, w)) == 1 for w in t[n + 2:]) for g in t[1:n + 1]])