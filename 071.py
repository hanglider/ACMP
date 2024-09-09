n = int(input()) 
*a, = map(int, input().split())
t = []
for j in range(2**n):
    s = [0,0]
    for i in range(n):
        s[j >> i & 1] += a[i]
    t += [abs(s[0]-s[1])]
print(min(t))