d = open(0).read().split()
n = int(d[0])
r = d[1:n + 1]
g = [-1] * n
f = [0] * n
p = -1
k = 0
y = 1
for v, i in sorted(zip([int(s, 2) for s in r], range(n)))[::-1]:
    if v != p:
        if k and (v & p) != v:
            y = 0
        k += 1
        p = v
        for j in range(n):
            if r[i][j] == '1':
                g[j] = k - 1
    f[i] = k - 1
if y:
    print("YES")
    print(*f)
    print(*g)
else:
    print("NO")
