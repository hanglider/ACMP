*b, t = map(int, open(0).read().split())
q = [(b[0], 0, 0)]
d = {q[0]: 0}
for s in q:
    for i in range(3):
        for j in range(3):
            v = min(s[i], b[j] - s[j])
            w = [*s]
            w[i] -= v
            w[j] += v
            w = tuple(w)
            if w not in d:
                d[w] = d[s] + 1
                q += w,
print(min([d[s] for s in d if s[0] == t] or ['IMPOSSIBLE']))
