def f(r, k, m):
    if r < 1:
        return [0]
    c = min(m, round(r ** (1 / 3)) + 1)
    while c and k * c**3 >= r:
        t = c**3 <= r and f(r - c**3, k - 1, c)
        if t:
            return [c] + t
        c -= 1
r = f(int(input()), 8, 2000)
print(*r[:-1] if r else ["IMPOSSIBLE"])
