import re
s = [10]
d = {}
for t in re.split('(<[^>]*>)', open(0).read()):
    u = t.lower()
    if u[:6] == '<font ':
        x = u[12:-2]
        s += [int(x) + s[-1] * (x[0] in '+-')]
    elif u == '</font>':
        s.pop()
    elif u[:1] != '<':
        d[s[-1]] = d.get(s[-1], 0) + len(''.join(t.split()))
for k in sorted(d):
    if d[k]:
        print(k, d[k])
