a, b, c, e, s = map(int, input().split())
d = c - e
if s > c and d < 1:
    print('NO')
else:
    k = s > c and (s - c - 1) // d + 1
    r = ((k * (a + b) * c + (s - k * d) * a) * 200 + c) // (2 * c)
    print(f'{r // 100}.{r % 100:02}')
