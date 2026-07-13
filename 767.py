d = open(0).read().split()
n = int(d[0])
g = [[] for i in range(n)]
e = 0
for i in range(n):
    for j in range(i + 1, n):
        if d[1 + i * n + j] == '1':
            g[i].append(j)
            g[j].append(i)
            e += 1
t = [0] * n
u = [0] * n
v = [0] * n
c = 0
b = 0
for s in range(n):
    if v[s]:
        continue
    q = [(s, -1, 0)]
    while q:
        x, p, i = q.pop()
        if i == 0:
            c += 1
            t[x] = c
            u[x] = c
            v[x] = 1
        if i < len(g[x]):
            q.append((x, p, i + 1))
            y = g[x][i]
            if not v[y]:
                q.append((y, x, 0))
            elif y != p:
                u[x] = min(u[x], t[y])
        else:
            if p >= 0:
                u[p] = min(u[p], u[x])
                if u[x] > t[p]:
                    b += 1
print(e - b)
