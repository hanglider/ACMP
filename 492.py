a, b, x, y, v, t, d = map(int, open(0).read().split())
s = (a + x * t)**2 + (b + y * t)**2
r = v * t
print(['NO', 'YES'][(d + r)**2 >= s and (d <= r or (d - r)**2 <= s)])
