import re
r = open(0).read().split('\n', 1)
w, b = map(int, r[0].split())
for p in re.split(r'\n\s*\n', r[1]):
    l = ' ' * (b - 1)
    for u in re.findall(r'[A-Za-z0-9]+[^A-Za-z0-9]*', p):
        u = ''.join(u.split())
        if len(l) + len(u) < w:
            l += ' ' + u
        else:
            print(l)
            l = u
    if l.strip():
        print(l)
