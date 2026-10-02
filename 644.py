from functools import cache
@cache
def f(b, c, x):
    h = 1 << b - 1
    if b < 9:
        s = 0
        while x < 2 * h:
            x += c + bin(x).count("1")
            s += 1
        return s, x
    if x < h:
        s, x = f(b - 1, c, x)
        if x >= 2 * h:
            return s, x
        t, x = f(b - 1, c + 1, x - h)
        return s + t, x + h
    s, x = f(b - 1, c + 1, x - h)
    return s, x + h
n, k = map(int, input().split())
while k:
    for b in range(45, 8, -1):
        s, x = f(b, bin(n >> b).count("1"), n % 2**b)
        if s <= k:
            k -= s
            n = (n >> b << b) + x
            break
    else:
        n += bin(n).count("1")
        k -= 1
print(n)
