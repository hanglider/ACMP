s = ''.join(x for x in open(0).read().split() if x in 'lr')
k = s.count('l') - s.count('r')
s += ['', 'r', '', 'l'][k % 4]
print(['TRUE', 'FALSE'][2 * 'rl'[k < 0] in s + s[0]])
