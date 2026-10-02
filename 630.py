from itertools import accumulate as u
i = (int(x) for l in open(0) for x in l.split())
for _ in range(next(i)):
    g = [(next(i), next(i)) for _ in range(next(i))]
    c = [0] * 10001
    for a, b in g:
        c[a] += 1
        c[b] -= 1
    s = list(u(c))[:-1]
    o = [0, *u(x == 1 for x in s)]
    print(["Wrong Answer", "Accepted"][0 not in s and all(o[b] > o[a] for a, b in g)])
