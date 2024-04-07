s = str(input())
k = int(input())
l = s
if k > 0:
    while (len(l) < 1024) and (k>1):
        l += s
        k -= 1
    print(l[:1023])
else:
    t = len(s) // abs(k)
    p = s[:t]
    if p*abs(k) == s:
        print(p[:1023])
    else:
        print('NO SOLUTION')