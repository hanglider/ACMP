n = int(input())
h = list(map(int, input().split()))
d = [0] * n
if n > 1:
    d[1] = abs(h[1] - h[0])
for i in range(2, n):
    d[i] = min(d[i-1] + abs(h[i] - h[i-1]), d[i-2] + 3 * abs(h[i] - h[i-2]))
print(d[n-1])
