from collections import Counter
from operator import add, mul, sub
r = open(0).read().split()
n = int(r[0])
x = list(map(int, r[1::2]))
y = list(map(int, r[2::2]))
w = [a * a + b * b for a, b in zip(x, y)]
c = [a * 2**33 + b for a, b in zip(x, y)]
t = {2 * q for q in c}
l = []
s = -n * n
for a, b, q in zip(x, y, c):
    k = Counter(map(sub, w, map(add, map((2 * a).__mul__, x), map((2 * b).__mul__, y)))).values()
    s += sum(map(mul, k, k)) - 2 * sum(map(t.__contains__, map(q.__add__, l)))
    l += q,
print(s // 2)
