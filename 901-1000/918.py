from heapq import *
n, *a = map(int, open(0).read().split())
h = []
for t, c in sorted(zip(a[::2], a[1::2])):
    heappush(h, c)
    if len(h) > t:
        heappop(h)
print(sum(h))
