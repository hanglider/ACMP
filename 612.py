def r(s):
    t = ''
    for c in s:
        if t[-1:] == c.swapcase():
            t = t[:-1]
        else:
            t += c
    return t
X, Y = open(0).read().split()
x = r(X)
y = r(Y)
l = 0
h = min(len(x), len(y)) + 1
while h - l > 1:
    m = (l + h) // 2
    if {x[k:k + m] for k in range(len(x) - m + 1)} & {y[k:k + m] for k in range(len(y) - m + 1)}:
        l = m
    else:
        h = m
d = {x[k:k + l]: k for k in range(len(x) - l + 1)}
j = next(k for k in range(len(y) - l + 1) if y[k:k + l] in d)
i = d[y[j:j + l]]
print(r(x[:i] + y[:j][::-1].swapcase()) + Y + r(y[j + l:][::-1].swapcase() + x[i + l:]))
