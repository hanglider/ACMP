L = 0
R = 1e18.__trunc__()
n, x, y = map(int, input().split())
n -= 1
time = min(x,y)
index = -1
if n == 0:
    print(time)
else:
    while R > L + 1:
        mid = (L + R) // 2
        t = (mid // x + mid // y)
        if t >= n:
            R = mid 
        else:
            L = mid 
    print(R+time)