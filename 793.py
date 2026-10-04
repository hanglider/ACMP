r = ''
for x in map(int, open(0).read().split()):
    n = x
    f = ''
    d = 2
    while d * d <= n:
        while n % d < 1:
            f += str(d)
            n //= d
        d += 1
    f += str(n) * (n > 1)
    s = lambda t: sum(map(int, t))
    r += str(+(n < x and s(f) == s(str(x))))
print(r)
