import fractions
import math
s = set()
for i in range(1, int(input())+1): 
    for j in range(1, i): 
        a, b = j, i
        t = math.gcd(a,b)
        while t != 1:
            a //= t
            b //= t
            t = math.gcd(a,b)
        s |= {fractions.Fraction(a,b)}
print("\n".join([str(i) for i in sorted(s)]))