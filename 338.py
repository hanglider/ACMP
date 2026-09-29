n, m, *a = open(0).read().split()
m = int(m)
s = ''.join(a)
v = set()
r = 0
for i in range(len(s)):
    if s[i] < '1' and i not in v:
        r += 1
        t = [i]
        v.add(i)
        while t:
            j = t.pop()
            for k in j - m, j + m, j - 1 if j % m else -1, j + 1 if (j + 1) % m else -1:
                if 0 <= k < len(s) and s[k] < '1' and k not in v:
                    v.add(k)
                    t.append(k)
print(r)
