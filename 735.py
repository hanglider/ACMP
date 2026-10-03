a, b = open(0).read().split()
s = a + '#' + b
m = len(s)
z = [0] * m
l = r = 0
for i in range(1, m):
    if i < r:
        z[i] = min(r - i, z[i - l])
    while i + z[i] < m and s[z[i]] == s[i + z[i]]:
        z[i] += 1
    if i + z[i] > r:
        l, r = i, i + z[i]
k = len(a) + 1
c = len(b)
for i in range(c - 1, -1, -1):
    if z[k + i] >= c - i:
        c = i
print(['NO', 'YES'][b[:c] in a])
