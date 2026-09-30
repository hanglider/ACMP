t = open(0).read().split()
n = int(t[0])
print('YNEOS'[any('.BG R'.find(c) & ~int(v) for c, v in zip(''.join(t[2:2 + n]), t[2 + n:]))::2])
