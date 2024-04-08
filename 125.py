def solve():
    n = int(input())
    a = []
    for i in range(n+1):
        a.append(list(map(int, input().split())))
    ans = 0
    col = list(map(int, input().split()))
    #если узлы ребра имеют одинаоквый цвет, то ans += 1
    for i in range(n):
        for j in range(n):
            if (a[i][j] == 1) & (col[i] != col[j]):
                ans += 1
    print(ans//2)
t = 1
#t = int(input())
while t > 0:
    solve() 
    t -= 1