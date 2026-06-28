from heapq import *
q = list(map(int, open('input.txt').read().split()))[1:]
heapify(q)
c = 0
while len(q) > 1:
    s = heappop(q) + heappop(q)
    c += s
    heappush(q, s)
print(f"{c*.05:.2f}")
