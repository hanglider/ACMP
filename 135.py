a = [list(map(int, input().split())) for i in range(int(input()))]
for k in range(len(a[0])):
    for i in range(len(a[0])):
        for j in range(len(a[0])):
            a[i][j] = min(a[i][j],a[i][k] + a[k][j])
for r in a:
    print(" ".join(map(str, r)))