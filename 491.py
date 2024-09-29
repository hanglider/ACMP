s = str(input())
bc = set(s)
if bc.__len__() == 1:
    print('NO SOLUTION')
else:
    sr = s[::-1]
    if sr == s:
        print(s[:len(s)-1])
    else:
        print(s)