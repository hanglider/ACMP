n, *a = open(0).read().split()
p = 1
for x in a:
    p *= 2 * float(x) - 1
print(round((1 + p) / 2, 6))
