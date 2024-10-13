a, b, c = map(int, input().split())
n = int(input())
p = (a+b+c) / 2
s = (p*(p-a)*(p-b)*(p-c)) ** (0.5)
r = s / p
if r >= n: print('YES')
else: print('NO')