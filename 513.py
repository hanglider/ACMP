import math
n = int(input())
ans = 0
for k in range(2, n+1):
    ans += (math.factorial(n) // (math.factorial(n-k)*math.factorial(k)))
print(ans)