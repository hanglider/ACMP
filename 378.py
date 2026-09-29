n, *a = map(int, open(0).read().split())
b = 1
for x in a:
    b |= b << x
print(bin(b).count("1"))
