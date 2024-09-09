n = int(input())
*a, = map(int, input().split())
s = 0
for i in range(n):
    s += max(a[i:n])
print(s)