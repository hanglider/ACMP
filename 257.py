p = [*map(int, open(0).read().split())]
if any(p):
    r = set()
    while p[-1] == 0:
        p.pop()
        r.add(0)
    d = abs(p[-1])
    for i in range(1, int(d**.5) + 2):
        if d % i < 1:
            for x in i, -i, d // i, -d // i:
                if sum(c * x**k for k, c in enumerate(p[::-1])) == 0:
                    r.add(x)
    print(len(r), *sorted(r))
else:
    print(-1)
