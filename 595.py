d = open(0).read().split()
a = d[0]
b = d[1]
n = len(a)
if n != len(b):
    print("No")
else:
    s = b + "#" + a
    m = 2 * n + 1
    z = [0] * m
    l = 0
    r = 0
    for i in range(1, m):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < m and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    c = b[::-1]
    p = 0
    while p < n and a[p] == c[p]:
        p += 1
    k = -1
    for j in range(n + 1):
        if j <= p and (j == n or z[n + 1 + j] >= n - j):
            k = j
            break
    if k < 0:
        print("No")
    else:
        print("Yes")
        print(k)
