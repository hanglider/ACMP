import re
s = input().strip()
n = len(s)
m = 1
while m * (m + 1) < 2 * n:
    m += 1
o = list(range(1, m + 1, 2))
e = list(range(2, m + 1, 2))
d = {}
i = 0
for k in e + o[::-1]:
    c = min(k, n - k * (k - 1) // 2)
    d[k] = s[i:i + c]
    i += c
p = re.findall('[A-Z][a-z]*', ''.join(d[k] for k in o + e[::-1]))
q = len(p) + 1
f = bytearray([1]) * q
for i in range(2, int(q**.5) + 1):
    if f[i]:
        f[i * i::i] = bytes(len(range(i * i, q, i)))
print(''.join(p[i - 1] for i in range(2, q) if f[i]) or 'Impossible')
