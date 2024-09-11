def solve(a):
    tmp = str(int(a[3:]) + 1).zfill(3)
    tmp1 = str(int(a[3:]) - 1).zfill(3)
    if int(a[0]) + int(a[1]) + int(a[2]) == int(tmp[0]) + int(tmp[1]) + int(tmp[2]) or int(a[0]) + int(a[1]) + int(a[2]) == int(tmp1[0]) + int(tmp1[1]) + int(tmp1[2]):
        return 'Yes'
    else:
        return 'No'
 
for _ in range(int(input())):
    print(solve(input()))