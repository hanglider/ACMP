n, *a = open(0).read().split()
n = int(n)
s = ''.join(r[::1 - i % 2 * 2] for i, r in enumerate(a))
k = s.count('C') // 2
p = 0
while k:
    k -= s[p] == 'C'
    p += 1
t = '1' * p + '2' * (n * n - p)
for i in range(n):
    print(t[i * n:i * n + n][::1 - i % 2 * 2])
