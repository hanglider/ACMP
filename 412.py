a, b, c, d, e, f = [ord(x) for x in input() if x > ' ']
u = e - c
v = f - d
m = max(abs(u), abs(v))
print(['NO', 'YES'][u * v * (u * u - v * v) == 0 and all((c + u * i // m, d + v * i // m) != (a, b) for i in range(1, m))])
