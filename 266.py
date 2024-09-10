n = {i for i in range(1440)}
for _ in range(int(input())):
    c, m, v, t = map(int, input().split())
    l = 60 * c + m 
    r = 60 * v + t
    if (c == v) & (m == t):
        continue
    if r < l:
        n &= {i for i in range(r)} | {i for i in range(l, 1440)}
    else:
        n &= {i for i in range(l, r)}
print(len(n))