n, k = map(int, input().split())
r = 0
for i in range(n):
    r = (r + k) % (i + 1)
print(r + 1)
