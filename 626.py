*r, t = open(0).read().split()
r = set(r[1:])
s = []
for c in t:
    if s and s[-1] + c in r:
        s.pop()
    else:
        s += c
print(''.join(s))
