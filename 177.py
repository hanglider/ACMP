n, m, *a = map(int, open(0).read().split())
f = a[:n]
g = a[n:]
w = {}
for t, i in sorted([(g[3 * i + 1], i) for i in range(m)] + [(g[3 * i + 2], i) for i in range(m)]):
    s = g[3 * i]
    if t == g[3 * i + 1]:
        o = [(f[y], y) for y in range(n) if f[y] >= s]
        k = [(g[3 * j], f[y], f[z] - g[3 * j], j, z, y) for j, y in w.items() for z in range(n) if z != y and f[z] >= g[3 * j] and f[y] + g[3 * j] >= s]
        if o:
            y = min(o)[1]
        elif k:
            *_, j, z, y = min(k)
            f[y] += g[3 * j]
            f[z] -= g[3 * j]
            w[j] = z
            print(f"move cargo {j + 1} from cell {y + 1} to cell {z + 1}")
        else:
            print(f"cargo {i + 1} cannot be stored")
            continue
        f[y] -= s
        w[i] = y
        print(f"put cargo {i + 1} to cell {y + 1}")
    elif i in w:
        y = w.pop(i)
        f[y] += s
        print(f"take cargo {i + 1} from cell {y + 1}")
