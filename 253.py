a, b, c, d = map(int, open(0).read().split())
s = a * 60 + b
print(sum(t % 60 == 30 if t % 60 else t // 60 % 12 or 12 for t in range(s, s + (c * 60 + d - s) % 1440)))
