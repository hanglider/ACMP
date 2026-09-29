from collections import Counter as C
*a, b = open(0).read().split()
print(sum(not C(w) - C(b) for w in a[1:]))
