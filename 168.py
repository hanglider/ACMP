string = ""
for i in range(1, 10001):
    string+=str(i)
print(string.find(input()) + 1)