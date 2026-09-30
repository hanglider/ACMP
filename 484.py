p = int(input()) - 1
f = [1, 2]
for _ in f * 19:
    f += [f[-1] + f[-2]]
l = 0
while p >= f[l]:
    p -= f[l]
    l += 1
i = c = g = 0
t = 1
o = [1]
for k in range(l):
    if t and p >= f[l - k - 1]:
        p -= f[l - k - 1]
        i, c, t = i + c + 1, i + 1, 0
    else:
        i, c, t = i + c, i, 1
    g += f[k]
    o += [g + i + 1]
print(*o[::-1])
