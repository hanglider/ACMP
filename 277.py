a, b, c = map(int, input().split())
s = ''
for k, v in (a, ''), (b, 'x'), (c, 'y'):
    if k:
        t = str(k)
        if v and k * k == 1:
            t = t[:-1]
        s += '+' * (k > 0 < len(s)) + t + v
print(s or 0)
