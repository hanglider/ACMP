with open('input.txt', 'r') as f:
    data = f.read().split()

n = int(data[0])
a = [int(x) for x in data[1:n+1]]

i = n - 2
while i >= 0 and a[i] >= a[i + 1]:
    i -= 1

if i == -1:
    a.reverse()
else:
    j = n - 1
    while a[j] <= a[i]:
        j -= 1
    a[i], a[j] = a[j], a[i]
    a[i + 1:] = reversed(a[i + 1:])

print(*a)
