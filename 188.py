a = [1, 1]
n = int(input())
for i in range(2,n+1):
  a.append(i*a[i-1]+(i-1)*a[i-2])
print((n-1)*a[n-2])