m = int(input())
n = m
s = ""
p = ""
while n > 1:
    i = 2
    while i < 10:
        if n % i == 0:
            s += str(i)
            n //= i 
            break
        i += 1
    if i == 10:
        print(-1, -1)
        exit()
    i = 9
    while i > 1:
        if m % i == 0:
            p += str(i)
            m //= i 
            break
        i -= 1 
print(p[::-1], s[::-1])