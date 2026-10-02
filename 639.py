a = [s.split() for s in open(0) if " " in s.strip()]
print(len(a))
for x, y in sorted(a, key=lambda p: -float(p[0])):
    print(x, y)
