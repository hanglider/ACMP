a = [0, 1, 1, 2]
for i in range(4, 56):
    a += [a[-1] + a[-3] + 1]
print(a[int(input())])
