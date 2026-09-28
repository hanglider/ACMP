x, y = map(int, open(0).read().split())
if x == y:
    print(0)
elif x == 0 or y % x or y // x < 2:
    print(-1)
else:
    n = y // x
    s = 0
    d = 2
    while d * d <= n:
        while n % d == 0:
            s += d
            n //= d
        d += 1
    print(s + n * (n > 1))
