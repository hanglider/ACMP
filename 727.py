from array import array
n = int(input())
a = array("i")
p = array("h")
for i in range(n):
    b = [*map(int, input().split())]
    a += array("i", b)
    p += array("h", sorted(range(n), key=lambda j: -b[j]))
s = [i * n for i in range(n)]
v = [0] * n
o = [-1] * n
for i in range(n):
    while i + 1:
        j = p[s[i]]
        s[i] += 1
        k = a[i * n + j] * n - i
        if k > v[j]:
            v[j] = k
            o[j], i = i, o[j]
r = [0] * n
for j in range(n):
    r[o[j]] = j + 1
print(*r)
