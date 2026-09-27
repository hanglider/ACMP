s = open(0).read().split()
n = int(s[0])
a = set(s[1:n + 1])
b = set(s[n + 2:])
for t, x in ("Friends", a), ("Mutual Friends", a & b), ("Also Friend of", b - a):
    print((t + ": " + ", ".join(sorted(x))).strip())