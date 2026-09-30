from heapq import *
input()
a = list(map(int, input().split()))
k = int(input())
m = max(a)
d = [0] + [m**4] * m
h = [(0, 0)]
while h:
    e, r = heappop(h)
    if e == d[r]:
        for x in a:
            t = (r + x) % m
            f = e + (m - x) * m + 1
            if f < d[t]:
                d[t] = f
                heappush(h, (f, t))
w, j = divmod(d[k % m], m)
r = (k + w) // m
if d[k % m] == m**4:
    r = -1
elif j * m - w > k:
    c = s = 1 << k
    r = 0
    while c & -c > 1:
        e = 0
        for x in a:
            e |= c >> x
        c = e & ~s
        s |= e
        r += 1
    r = r if c else -1
print(r)
