m = map(int, open('input.txt').read().split()[1:])
p = sorted({*zip(m, m)})
s = 0
while p:
    x, y = p.pop()
    s += len({(v - y) / (u - x) if u - x else 1e9 for u, v in p})
print(2 * s)