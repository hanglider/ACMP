from fractions import Fraction as F
s = open(0).read().split()
x, y, r = int(s[0]), int(s[1]), F(s[2])
p = [(u - x, v - y) for u, v in zip(map(int, s[4::2]), map(int, s[5::2]))]
p = [(u, v) for u, v in p if u * u + v * v <= r * r]
print(max(sum(k * (u * z - v * w) >= 0 for w, z in p) for u, v in p + [(1, 0)] if u | v for k in (1, -1)))
