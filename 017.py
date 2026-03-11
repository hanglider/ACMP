n = int(input())
a = []
while len(a) < n:
    a += list(map(int, input().split()))

b = a[:-1]
m = n - 1

pi = [0] * m
for i in range(1, m):
    j = pi[i - 1]
    while j > 0 and b[i] != b[j]:
        j = pi[j - 1]
    if b[i] == b[j]:
        j += 1
    pi[i] = j

p = m - pi[-1]
if m % p == 0:
    print(p)
else:
    print(m)