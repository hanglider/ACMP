n = int(input())
s = ""
while n:
    n -= 1
    s = str(n % 3 + 1) + s
    n //= 3
print(s)
