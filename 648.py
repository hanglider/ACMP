import time
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    l = 0
    r =  l
    for i in range(n//2):
        l += a[i]
    for i in range(n//2,n):
        r += a[i]
    print(r - l)
    pass

t = 1
#t = int(input())
while t > 0:
    solve()
    t -= 1