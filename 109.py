s = input().strip()
x, y = map(int, s.split('/'))

a = x // y
x %= y

if x == 0:
    print(a)
else:
    d = {}
    b = []
    i = 0

    while x and x not in d:
        d[x] = i
        x *= 10
        b.append(str(x // y))
        x %= y
        i += 1

    if x == 0:
        print(str(a) + '.' + ''.join(b))
    else:
        i = d[x]
        print(str(a) + '.' + ''.join(b[:i]) + '(' + ''.join(b[i:]) + ')')