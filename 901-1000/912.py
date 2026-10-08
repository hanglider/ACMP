a = open(0).read().split()[1:]
s = set(a)
m = max(map(a.count, s))
b = [v for v in s if a.count(v) == m]
print([0, *b][len(b) < 2])
