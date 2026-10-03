from functools import *
f = cache(lambda n: n > 3 and f(n // 2) + f(n - n // 2) or n == 3)
print(+f(int(input())))
