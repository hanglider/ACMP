n = int(input())
s = bytearray([1]) * 10**6
for i in range(2, 999):
    if s[i]:
        s[i * i::i] = bytes(len(s[i * i::i]))
r = []
while n > 1:
    p = s.index(1, n + 1)
    r += [f'{i} {p - i}' for i in range(p - n, p // 2 + 1)]
    n = p - n - 1
print('\n'.join(r))
