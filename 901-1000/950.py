N = str(input())
mtx = []
count = 0
for i in range(len(N)):
    count+=1
    if N[i] == '1':
        mtx.append(count - 1)
        count = 0

dict = "abcdefghijklmnopqrstuvwxyz"
res = ""
for i in range(len(mtx)):
    res+=dict[mtx[i]]
print(res)