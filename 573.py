n, v, *r = open(0).read().split()
n = int(n)
p = [(int(r[3 * i][:2]) * 60 + int(r[3 * i][3:]), int(r[3 * i + 1]), int(r[3 * i + 2])) for i in range(n)]
m = [-1] * n
def f(i, u):
    for j in range(n):
        t = p[j][0] - p[i][0]
        if t > 0 and j not in u and 3600 * ((p[j][1] - p[i][1])**2 + (p[j][2] - p[i][2])**2) <= int(v)**2 * t * t:
            u.add(j)
            if m[j] < 0 or f(m[j], u):
                m[j] = i
                return 1
    return 0
print(n - sum(f(i, set()) for i in range(n)))
