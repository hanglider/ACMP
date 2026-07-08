N = int(input())
a = list(map(int, input().split()))
V = [a[N - 1 - u] for u in range(N)]
for m in range(1, N):
    mx = (N - 1 - m) % 2 == 0
    W = []
    for u in range(N - m):
        if mx:
            W.append(max(V[u], V[u + 1]))
        else:
            W.append(min(V[u], V[u + 1]))
    V = W
print(V[0])
