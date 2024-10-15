def f(x):
    if x == '6': return 6
    if x == '7': return 7
    if x == '8': return 8
    if x == '9': return 9
    if x == 'T': return 10
    if x == 'J': return 11
    if x == 'Q': return 12
    if x == 'K': return 13
    if x == 'A': return 14
 
n, m, c = map(str, input().split())
n = int(n)
m = int(m)
a = list(map(str, input().split()))
t = list(map(str, input().split()))
a1 = {}
t1 = {}
g = 0
 
for i in range(n):
    if a[i][1] == c:
        g = 100
    else:
        g = 0
    a1[i] = (a[i][1], f(a[i][0]) + g)
 
for i in range(m):
    if t[i][1] == c:
        g = 100
    else:
        g = 0
    t1[i] = (t[i][1], f(t[i][0]) + g)

work = sorted(a1.items(), key=lambda x: x[1][1])

a1 = {}
for i in range(n):
	a1[i] = (work[i][1][0], work[i][1][1])

 
for j in t1:
    F = False
    for i in a1:
        if ((a1[i][0] == t1[j][0]) & (a1[i][1] > t1[j][1])) or ((a1[i][0] == c) & (a1[i][1] > t1[j][1])): 
            F = True
            a1.pop(i)
            break
    if F == False:
        print("NO")
        raise SystemExit
 
print("YES")