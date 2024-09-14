import math
t = int(input())
p = math.factorial(t)
while p % 10 == 0:
    p = p // 10
print(p % 10)