n, m = map(int, input().split())
a = [[*map(int, input().split())] for _ in range(n)]
r = max(a, key=max)
c = r.index(max(r))
print(min(a, key=lambda x: x[c])[r.index(min(r))])
