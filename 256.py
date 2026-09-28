t = open(0).read().split()
a = b = 0
for c, k in zip(t[1::2], t[2::2]):
    a += int(k) * (c < 'Z')
    b += int(k) * (c > 'X')
print(max(abs(a), abs(b), abs(a - b)))
