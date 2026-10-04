a = input().split('/')
b = int(a[0]) + 1
r = []
for x in a:
    x = int(x)
    s = ''
    while x:
        s = '0123456789ABCDEFGHIJKLMNOPQRSTUV'[x % b] + s
        x //= b
    r += s,
print(*r, sep='/')
