def solve():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    ans = 100000
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if min(a[i][j] ,a[j][k], a[k][i]) != 0:
                    ans = min(a[i][j] + a[j][k] + a[k][i],ans)
    print(ans)
t = 1
#t = int(input())
while t > 0:
    solve() 
    t -= 1