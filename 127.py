import queue

def bfs(v, graph):
    q = queue.Queue()
    visited = [False]*n
    visited[v] = True
    q.put(v)
    while not q.empty():
        x = q.get()
    for i in graph[x]:
        if visited[i-1] == False:
            d[i-1][x] = min(d[i-1][x], min(d[x])+1)
        visited[i-1] = True
        q.put(i-1)


n = int(input())
graph = [[] for i in range(n)]
for i in range(n):
    *a, = map(int, input().split())
    for j in range(len(a)):
        if a[j] == 1:
        graph[i] += [j+1]
a, m = map(int, input().split())
d = [[99999]*n for i in range(n)]
d[a-1][a-1] = 0
bfs(a-1, graph)
if min(d[m-1]) == 99999:
    print(-1)
else:
    print(min(d[m-1]))