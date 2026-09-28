import re
k, *a = map(int, re.findall(r"\d+", open(0).read()))
c = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
t = sorted((c[a[i + 1] - 1] + a[i]) * 1440 + a[i + 2] * 60 + a[i + 3] for i in range(0, 4 * k, 4))
w = lambda x: x // 1440 * 480 + min(max(x % 1440 - 600, 0), 480)
s = sum(w(y + 1) - w(x) for x, y in zip(t[::2], t[1::2]))
print(f"{s // 60}:{s % 60:02}")
