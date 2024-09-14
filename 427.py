g = input
n = int(g())
a = [int(g()) for i in range(n)]
t = 0
a.sort()
for i in range(n):
    if a[i] > t + 1: break
    t += a[i]
print(t + 1)