def f(a):
    ans = 0
    while a > 0:
        ans += a % 10
        a = a // 10
    return ans

def solve():
    n = int(input())
    a = 1
    ans = 1
    chisla = []
    for i in range(2,n+1):
        if n % i == 0:
            chisla.append(i)
    for i in chisla:
        t = f(i)
        if t > a:
            a = t 
            ans = i
    print(ans)
    return 0

t = 1
#t = int(input())
while t > 0:
    solve()
    t -= 1