n = int(input())
a = []
c, b = 0, 0
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if a[i]==0: c+=1
    else: b+=1
print(min(b,c))