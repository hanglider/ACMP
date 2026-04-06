n = int(input())
x = list(map(int, input().split()))

a = []
for i in range(n):
    a.append((x[i], i + 1))

a.sort()

best = a[1][0] - a[0][0]
ans1 = a[0][1]
ans2 = a[1][1]

for i in range(1, n - 1):
    d = a[i + 1][0] - a[i][0]
    if d < best:
        best = d
        ans1 = a[i][1]
        ans2 = a[i + 1][1]

print(best)
print(ans1, ans2)