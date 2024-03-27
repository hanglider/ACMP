n = int(input())
t = [10**5]*(n+1) 
t[0] = 0
for j in range(n):
    *a, = map(int, input().split())
    for i in range(len(a)):
        f = i + j + 1
        t[f] = min(t[f], a[i]+t[j])
print(t[n])