H = int(input())
o = list(map(int, input().split()))
S = input()
L = len(S)
W = -(-L // H)
r = L - H * (W - 1)
l = [W if i <= r else W - 1 for i in range(1, H + 1)]
g = [None] * H
i = 0
for p in o:
    c = l[p - 1]
    g[p - 1] = S[i:i + c]
    i += c
R = ''
for c in range(W):
    for k in range(H):
        if c < l[k]:
            R += g[k][c]
print(R)
