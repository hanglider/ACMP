s = input()
a = max(s)
b = min(s)
p = q = -len(s)
r = s
for i, c in enumerate(s):
    if c == a:
        p = i
    if c == b:
        q = i
    if i - min(p, q) < len(r):
        r = s[min(p, q):i + 1]
print(r)
