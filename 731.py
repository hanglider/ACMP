n, *a = open(0).read().split()
c = list(map(int, a[1::2]))
s = sum(c)
f = [100 * x // s for x in c]
k = 100 - sum(f)
for i in sorted(range(int(n)), key=lambda i: a[2 * i]):
    if k and 100 * c[i] % s:
        f[i] += 1
        k -= 1
print(*f, sep='\n')
