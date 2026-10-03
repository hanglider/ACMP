a, b = [(ord(s[0]) - 65, int(s[1]) - 1) for s in input().split()]
d = {a: 0}
q = [a]
for x, y in q:
    for i in range(9):
        for j in range(9):
            u = abs(i - x)
            v = abs(j - y)
            if (i, j) not in d and ((x + y) % 2 and u * v == 2 or (x + y) % 2 < 1 and u == v > 0):
                d[i, j] = d[x, y] + 1
                q += [(i, j)]
print(d.get(b, -1))
