for x in open(0).read().split()[1:]:
    x = int(x)
    c = []
    for b in range(2, 37):
        s = ''
        y = x
        while y:
            s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[y % b] + s
            y //= b
        c += [(len(s) + len(set(s)), b, s)]
    print(*min(c)[1:])
