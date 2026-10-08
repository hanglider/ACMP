n, m = map(int, input().split())
ans = 1
b = 2
a = 1
for i in range(2, 2*n+1, 2):
    a *= i
    ans += a 
ans -= 1
print(ans % m)