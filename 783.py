s = open(0).read().split()
v = set()
c = 0
for i in range(64):
    if i not in v:
        c += 1
        q = [i]
        v.add(i)
        for k in q:
            x, y = divmod(k, 8)
            for a, b in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                j = a * 8 + b
                if 0 <= a < 8 and 0 <= b < 8 and j not in v and s[a][b] != s[x][y]:
                    v.add(j)
                    q.append(j)
print(c)
