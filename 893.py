import math
n = int(input())
if (n == 1) or (n == 2): print(n)
else: print(math.factorial(n) // math.factorial(n-3))