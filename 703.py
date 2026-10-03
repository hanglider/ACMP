r = open(0).read().split()
a = r[0] + r[2] + r[4]
b = r[1] + r[3] + r[5]
d = {a: 0}
q = [a]
for s in q:
    for i in range(9):
        for j in range(9):
            if s[i] > s[j] == "." and (i // 3 - j // 3)**2 + (i % 3 - j % 3)**2 == 5:
                t = list(s)
                t[i], t[j] = ".", s[i]
                t = "".join(t)
                if t not in d:
                    d[t] = d[s] + 1
                    q += t,
print(d.get(b, -1))
