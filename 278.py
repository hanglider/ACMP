s, t = open(0).read().split()
t = iter(t)
print(['NO', 'YES'][all(c in t for c in s)])
