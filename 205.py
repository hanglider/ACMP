a, b = open(0).read().split()
f = lambda s: sum(int(x) * 60**i for i, x in enumerate(s.split(':')[::-1]))
t = f(a) + f(b)
d = t // 86400
print('%02d:%02d:%02d' % (t // 3600 % 24, t // 60 % 60, t % 60) + '+%d days' % d * (d > 0))
