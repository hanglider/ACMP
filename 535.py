from itertools import permutations
f = lambda x, y: ''.join(str(int(p) + int(q)) for p, q in zip(x.zfill(len(y)), y.zfill(len(x))))
s = sorted({int(f(f(x, y), z)) for x, y, z in permutations(input().split())})
print('YNEOS'[len(s) < 2::2])
print(*s, sep='\n')
