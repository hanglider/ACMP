n = int(input())
b = 1
while b < n:
    b *= 2
print(min(n-b//2, b-n))