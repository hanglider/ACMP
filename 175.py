m = [63, 6, 91, 79, 102, 109, 125, 7, 127, 111]
h, s = map(int, input().split(":"))
t = h * 60 + s - 1
u = [95] + [127] * 3
o = [0] * 4
f = [0] * 4
while o + f != u + u:
    t += 1
    x = t % 1440
    d = [m[x // 600] * (x > 599), m[x // 60 % 10], m[x % 60 // 10], m[x % 10]]
    o = [a | b for a, b in zip(o, d)]
    f = [a | b & ~c for a, b, c in zip(f, u, d)]
print(t - h * 60 - s)
