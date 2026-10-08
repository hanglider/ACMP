from functools import cache
@cache
def f(a, b, c):
    if min(a, b, c) < 1:
        return 1
    if max(a, b, c) > 20:
        return f(20, 20, 20)
    if a < b < c:
        return f(a, b, c - 1) + f(a, b - 1, c - 1) - f(a, b - 1, c)
    return f(a - 1, b, c) + f(a - 1, b - 1, c) + f(a - 1, b, c - 1) - f(a - 1, b - 1, c - 1)
print(f(*map(int, input().split())))
