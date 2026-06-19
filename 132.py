import heapq

with open("input.txt") as f:
    data = f.read().split()

idx = 0
n = int(data[idx]); idx+=1
s = int(data[idx])-1; idx+=1
fin = int(data[idx])-1; idx+=1

g = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        g[i][j] = int(data[idx]); idx+=1

INF = float('inf')
dist = [INF]*n
dist[s] = 0
pq = [(0, s)]
while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v in range(n):
        w = g[u][v]
        if w != -1 and u != v:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

print(dist[fin] if dist[fin] != INF else -1)
