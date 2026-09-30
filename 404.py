from math import isqrt
n = int(input())
s = isqrt(n)
d = n - s * s - 2 * s + 2 * (1 << s.bit_length() - 1) - 1
print("LOSE" if d in (0, s + 1) else "WIN")
