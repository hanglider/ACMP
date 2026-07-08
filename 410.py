import heapq
n, m = map(int, open('INPUT.TXT').read().split())
t = -n % m
if t == 0:
    print(0)
else:
    h = [(d, 1, str(d), d % m) for d in range(1, 10)]
    heapq.heapify(h)
    v = [0] * m
    while h:
        c, l, s, r = heapq.heappop(h)
        if v[r]:
            continue
        v[r] = 1
        if r == t:
            print(s)
            break
        for d in range(10):
            q = (r * 10 + d) % m
            if not v[q]:
                heapq.heappush(h, (c + d, l + 1, s + str(d), q))
