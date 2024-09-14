def lcm(a,b):
    m = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)
n, m = map(int, input().split())
if m % n == 0:
    print(1)
    raise SystemExit
print(lcm(n,m)//m)