s = [*map(int, open(0).read().split())]
n, c, p = s[:3]
z = [complex(*s[i:i + 2]) for i in range(3, len(s), 2)]
q = z.pop()
print("YNEOS"[min(abs(q - a) + sum(abs(a - b) for b in z) for a in z) * c > p::2])
