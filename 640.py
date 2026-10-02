from itertools import dropwhile
d = open(0).read().split()
n = int(d[0])
c = []
for g in d[2:2 + n], d[4 + n:]:
    for _ in range(4):
        g = list(zip(*dropwhile(lambda s: "#" not in s, g)))[::-1]
    c += g,
x, y = c
s = []
for _ in range(4):
    x = list(zip(*x[::-1]))
    s += x, x[::-1]
print("YNeos"[y not in s::2])
