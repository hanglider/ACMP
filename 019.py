P = input().split()
S = set()
def C(s):
    return ord(s[0]) - 65, int(s[1]) - 1

Q, R, N = [C(p) for p in P]
O = {Q, R, N}

qc, qr = Q
for i in range(8):
    S.add((i, qr))
    S.add((qc, i))
for d in range(-7, 8):
    if 0 <= qc + d < 8 and 0 <= qr + d < 8:
        S.add((qc + d, qr + d))
    if 0 <= qc + d < 8 and 0 <= qr - d < 8:
        S.add((qc + d, qr - d))

rc, rr = R
for i in range(8):
    S.add((i, rr))
    S.add((rc, i))

nc, nr = N
for dx, dy in [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]:
    x, y = nc + dx, nr + dy
    if 0 <= x < 8 and 0 <= y < 8:
        S.add((x, y))

print(len(S - O))
