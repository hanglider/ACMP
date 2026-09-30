n = input()
k = 0
while n != '6174':
    s = sorted(n)
    n = '%04d' % (int(''.join(s[::-1])) - int(''.join(s)))
    k += 1
print(6174)
print(k)
