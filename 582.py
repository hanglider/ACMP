s = {tuple(input().split())}
for _ in range(6):
    s |= {(p[5], p[4], p[2], p[3], p[0], p[1]) for p in s} | {(p[2], p[3], p[1], p[0], p[4], p[5]) for p in s}
print(['NO', 'YES'][tuple(input().split()) in s])
