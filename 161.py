n, *a = map(int, open(0).read().split())
s = [*range(1, n + 1)]
print(*[s.pop(~x) for x in a[::-1]][::-1])
