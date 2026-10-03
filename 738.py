s = input()
k = sorted(s, key=lambda c: (-s.count(c), c))
t = {5: '43210 42103 31420 30142 23041 21304 14023 10234 04312 02431', 7: '40321 34201 23014 02143 01432', 9: '42301 20143'}
for w in t.get(sum(map(s.count, s)), '01234').split():
    print(''.join(k[int(c)] for c in w))
