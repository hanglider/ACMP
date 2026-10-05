n, b = open(0).read().split()
b = b[::-1]
t = r = ''
for i in range(int(n)):
    c = b[2**i - 1]
    r = c + r
    t = t + c + t[::-1].translate({79: 75, 75: 79})
print(r.translate({79: 80, 75: 90}) if t == b else 'NO')
