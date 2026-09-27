t = open(0).read().split()
p = complex(float(t[0]), float(t[1]))
r = []
for i in range(int(t[2])):
    v = [complex(float(t[3 + 6 * i + 2 * j]), float(t[4 + 6 * i + 2 * j])) for j in range(3)]
    s = [((v[j - 1] - v[j]).conjugate() * (p - v[j])).imag for j in range(3)]
    if min(s) > 0 or max(s) < 0:
        r.append(i + 1)
print(len(r))
print(*r)