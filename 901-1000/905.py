n, *l = open(0).read().split('\n')
l = [s.strip('\r') for s in l[:int(n)]]
k = 'the quick brown fox jumps over the lazy dog'
r = 'No solution'
for s in l:
    p = set(zip(s, k))
    if len(s) == 43 and len(p) == len(set(s)) == 27 and (' ', ' ') in p:
        r = '\n'.join(t.translate(str.maketrans(dict(p))) for t in l)
print(r)
