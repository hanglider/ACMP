a, b, c, e = open(0).read().split()
s = a + b
t = c + e
d = {s: 0}
q = [s]
for s in q:
    i = s.find('#')
    for j in i ^ 4, i - 1, i + 1:
        if j // 4 == i // 4 or j == i ^ 4:
            l = list(s)
            l[i], l[j] = l[j], l[i]
            u = ''.join(l)
            if u not in d:
                d[u] = d[s] + 1
                q += [u]
print(d.get(t, -1))
