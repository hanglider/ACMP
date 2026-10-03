from itertools import product
n, *f = open(0).read().split()
f = ''.join(f)
n = int(n)
b = -1, 'No solution'
for t in product('01', repeat=n if n < 8 else 5):
    s = r = ''.join(t)
    if n > 7:
        r = s[:2] + s[2] * (n - 4) + s[3:]
        s = s[:2] + s[2] * (2 + n % 2) + s[3:]
    v = int(s[0])
    for c in s[1:]:
        v = int(f[2 * v + int(c)])
    if v and r.count('1') > b[0]:
        b = r.count('1'), r
print(b[1])
