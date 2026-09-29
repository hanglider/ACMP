n, *p = open(0).read().split()
i = p.index('1')
print(*p[i:] + p[:i])
