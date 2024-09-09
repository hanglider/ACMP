def cnv(n):
    if n == 0:
        return 0
    
    if n > 0:
        return int(''.join(sorted(str(n), reverse=True)))
    else:
        s = sorted(str(abs(n)))
        k = 0
        while s[k] == '0':
            k += 1
        s = s[k] + '0' * (k) + ''.join(s[k+1:])
        return -int(s)

a = int(input())
b = int(input())
print(cnv(a) + cnv(-b))