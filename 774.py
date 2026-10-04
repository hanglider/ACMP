from fractions import Fraction as F
n, m, r, h, *s = open(0).read().split()
n = int(n)
c = [sum(F(r)**2 >= x * x * F(k) for k in ('.5', '1.25', '425/256', '2', '2.5')) * (F(h) // x) for x in map(F, s[:n])]
print(max(int(q) * c[i % n] for i, q in enumerate(s[n:])))
