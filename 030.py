h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
a = h1 * 3600 + m1 * 60 + s1
b = h2 * 3600 + m2 * 60 + s2
c = [0] * 10
for t in range(a, b + 1):
    h = t // 3600
    m = t // 60 % 60
    s = t % 60
    r = "%02d%02d%02d" % (h, m, s)
    for x in r:
        c[int(x)] += 1
for x in c:
    print(x)
