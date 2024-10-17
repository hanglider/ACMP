a, b, n = map(int, input().split())
l = 0
r = 1e18.__trunc__()
while r > l + 1:
    m = (l + r) // 2
    if (m // a) * (m // b) >= n:
        r = m
    else:
        l = m 
print(r)