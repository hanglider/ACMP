s = 0
c = 3
for x in open(0).read().split()[1:]:
    if x > '0':
        s += c
        c += 1
    else:
        c = max(3, c - 3)
print(s)
