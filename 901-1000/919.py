from math import gcd
a, b, w, h = map(int, open(0).read().split())
g = gcd(a, b)
r = lambda n: n % g < 1 and n // g * pow(a // g, -1, b // g) % (b // g) * a <= n
print("YES" if w % a + h % b < 1 or w % b + h % a < 1 or w % a + w % b < 1 and r(h) or h % a + h % b < 1 and r(w) else "NO")
