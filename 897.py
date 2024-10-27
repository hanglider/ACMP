import math
t = int(input())
a = list(map(int, input().split()))
for i in range(t):
    f = False
    for j in range(2,math.sqrt(a[i]).__trunc__() + 1):
        if f == True:
            break
        k = a[i]
        while k % j == 0:
            k = k // j
            if k == 1:
                print('YES')
                f = True
                break
    if f == False:
        print('NO')