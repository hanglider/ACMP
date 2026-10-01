n, *g = open(0).read().split()
m = len(g[1]) + 2
s = 'x' * m + ''.join('x' + r + 'x' for r in g[1:]) + 'x' * m
print(sum(s[i] == '.' and '*' not in s[i - 1] + s[i + 1] + s[i - m] + s[i + m] for i in range(m, len(s) - m)))
