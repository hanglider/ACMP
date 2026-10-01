n, *v = map(float, open(0).read().split())
a = v[::2]
b = v[1::2]
o = sorted(range(int(n)), key=lambda i: a[i] / b[i])[::-1]
s = sum(b)
p = 0
for i in o:
    s -= b[i]
    if p + a[i] >= s:
        print("%.3f" % (p + a[i] * (s + b[i] - p) / (a[i] + b[i])))
        break
    p += a[i]
print(*[i + 1 for i in o])
