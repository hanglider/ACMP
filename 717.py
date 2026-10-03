t = open(0).read().split()
n = int(t[0])
g = [0]
j = n + 1
for i in range(n):
    k = int(t[j])
    g.append(t[j + 1:j + k + 1])
    j += k + 1
u = [0] * (n + 1)
s = [1]
r = []
while s:
    v = s.pop()
    if v < 0:
        r.append(~v)
    elif u[v] < 1:
        u[v] = 1
        s.append(~v)
        s += map(int, g[v])
print(sum(int(t[v]) for v in r), len(r))
print(*r)
