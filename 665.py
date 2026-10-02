h, m = map(int, input().split(':'))
t = h * 60 + m
while 1:
    t = (t + 1) % 1440
    s = '%02d:%02d' % divmod(t, 60)
    if s == s[::-1]:
        break
print(s)
