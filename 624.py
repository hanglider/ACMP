a = list(map(int, open(0).read().split()))
p = 1
for _ in range(a[0]):
    n = a[p]
    p += 2
    L = []
    for i in range(n):
        k = a[p]
        L.append(a[p + k:p:-1])
        p += k + 1
    s = set()
    w = {}
    q = list(range(n))
    while q:
        i = q.pop()
        l = L[i]
        while l:
            x = l[-1]
            if x < 0 and -x not in s:
                w[-x] = i
                break
            l.pop()
            s.add(x)
            if x in w:
                q.append(w.pop(x))
    print('NO' if w else 'YES')
