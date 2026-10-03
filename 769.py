n, *s = open(0).read().split()
s = sorted(set(s)) + ['']
print(sum(not b.startswith(a) for a, b in zip(s, s[1:])))
