n, m = map(int, input().split(' '))
string = input()[:n]
count = []
for i in range(len(string)-m+1):
    if string[i:i+m] not in count:
        count.append(string[i:i+m])
print(len(count))