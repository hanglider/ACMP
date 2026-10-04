l = [s.rstrip() for s in open(0) if s.strip()]
n = ['Fedya', l[0][10:-10]]
for i, s in enumerate(l[1:-1]):
    s = s[10:]
    if s[-1] == '.':
        s = s[:-1]
    if s[-1] not in '!?':
        s += ','
    print('"' + s + '" --- skazal ' + n[i % 2] + '.')
