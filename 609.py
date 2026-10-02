L = [l.split() for l in open(0) if l.strip()]
i = 0
o = []
while L[i] != ['0', '0']:
    n, k = map(int, L[i])
    A = [list(map(int, l)) for l in L[i + 1:i + k + 1]]
    i += k + 1
    u = []
    while A:
        a = A.pop()
        y = [x for x in u if x > a[-1]]
        while not y and a[1:]:
            u.append(a.pop())
            y = [x for x in u if x > u[-1]]
        if y:
            A.append(a + [min(y)])
            break
        u += a
    A += [[x] for x in range(1, n + 1) if all(x not in a for a in A)]
    o.append("%d %d\n" % (n, len(A)) + "\n".join(" ".join(map(str, a)) for a in A))
print("\n\n".join(o))
