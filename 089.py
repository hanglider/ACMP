L = open(0).read().splitlines()
r = []
for s in L[1:int(L[0]) + 1]:
    k = s.rindex('"') + 1
    a, b = [int(h) * 60 + int(m) for h, m in (x.split(':') for x in s[k:].split())]
    r.append(((b - a) % 1440 or 1440, s[s.index('"'):k]))
d, q = min(r)
print('The fastest train is %s.\nIts speed is %d km/h, approximately.' % (q, (78000 + d) // (2 * d)))