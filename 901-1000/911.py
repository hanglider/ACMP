c, n = input().split()
n = int(n)
r = [[], [], []]
k = 1
while n:
    r[n % 3].append(k)
    n = (n + 1) // 3
    k *= 3
for i in 'LR':
    print(i + ':' + ' '.join(map(str, r[1 + (i == c)])))
