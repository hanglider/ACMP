n = int(input())
a = list(map(int, input().split()))
L = [0] * n
R = [0] * n
m = -10**9
for i in range(n):
    L[i] = m
    if a[i] > m:
        m = a[i]
m = -10**9
for i in range(n - 1, -1, -1):
    R[i] = m
    if a[i] > m:
        m = a[i]
r = [a[i] for i in range(n) if L[i] <= a[i] or R[i] <= a[i]]
print(len(r))
print(*r)
