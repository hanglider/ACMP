from collections import deque, defaultdict

d = open('input.txt').read().split()
k, s = int(d[1]), d[2]

g, q = deque([(0, 0)]), defaultdict(deque)
q[s[0]].append((0, 0))

for i, c in enumerate(s[1:], 1):
    while g and g[0][0] < i - k: g.popleft()
    while q[c] and q[c][0][0] < i - k: q[c].popleft()
    
    v = min(g[0][1] + 1, q[c][0][1] if q[c] else 1e9)
    
    while g and g[-1][1] >= v: g.pop()
    while q[c] and q[c][-1][1] >= v: q[c].pop()
    
    g.append((i, v))
    q[c].append((i, v))

print(v)
