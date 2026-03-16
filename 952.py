n, m = map(int, input().split())

if n == 0 and m > 0:
    print('Impossible')
else:
    x = max(n, m)
    if m == 0:
        y = n
    else:
        y = n + m - 1
    print(x, y)