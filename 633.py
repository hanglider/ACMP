t, *s = open(0).read().splitlines()
print(t + ":", ", ".join(sorted(s[:3])))
