n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(str, input().split(' '))))
for i in range(len(arr)):
    for j in range(len(arr[i])):
        tmp = arr[i][j]
        if tmp[0] == '-':
            tmp = tmp[1:]
            arr[i][j] = (-1)*int(tmp)
        else:
            arr[i][j] = int(tmp)

minArr = []
maxArr = []
for i in range(n):
    minArr.append(min(arr[i]))

for i in range(m):
    c = [r[i] for r in arr]
    maxArr.append(max(c))

print(max(minArr), min(maxArr))