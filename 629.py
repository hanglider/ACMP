from math import comb
n, k, m = map(int, open(0).read().split())
m -= 1
s = ''
i = 0
while k:
    c = comb(n - i - 1, k - 1)
    if m < c:
        s += chr(97 + i)
        k -= 1
    else:
        m -= c
    i += 1
print(s)
