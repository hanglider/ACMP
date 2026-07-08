from collections import deque
K = int(input())
S = input()
n = len(S)
q = [deque() for _ in range(26)]
c = [0] * 26
m = 0
u = [False] * n
p = 0
R = []
for i in range(n):
    while p <= i + K and p < n:
        x = ord(S[p]) - 97
        if c[x] == 0:
            m |= 1 << x
        c[x] += 1
        q[x].append(p)
        p += 1
    f = i - K
    if f >= 0 and not u[f]:
        x = ord(S[f]) - 97
        q[x].popleft()
        u[f] = True
        c[x] -= 1
        if c[x] == 0:
            m &= ~(1 << x)
        R.append(chr(x + 97))
    else:
        l = m & (-m)
        x = l.bit_length() - 1
        j = q[x].popleft()
        u[j] = True
        c[x] -= 1
        if c[x] == 0:
            m &= ~(1 << x)
        R.append(chr(x + 97))
print(''.join(R))
