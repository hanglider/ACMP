from math import comb


def g(r, k):
    p = [1] + [0] * k
    for x in r:
        q = [0] * (k + 1)
        for j in range(k + 1):
            for t in range(min(x, k - j) + 1):
                q[j + t] += p[j] * comb(k - j, t)
        p = q
    return p[k]


def f(x):
    s = str(x)
    n = len(s)
    a = 0
    for l in range(1, n):
        a += 9 * g([1] + [2] * 9, l - 1)
    r = [2] * 10
    for i in range(n):
        for d in range(i < 1, int(s[i])):
            if r[d]:
                r[d] -= 1
                a += g(r, n - i - 1)
                r[d] += 1
        r[int(s[i])] -= 1
        if r[int(s[i])] < 0:
            return a
    return a + (x > 0)


l, r = map(int, input().split())
print(f(r) - f(l - 1))
