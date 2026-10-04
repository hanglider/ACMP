n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    s = input()
    for j in range(m):
        (a, b)[(s[j] > 'V') ^ (i + j) % 2].append(f'{i + 1} {j + 1}')
r = min(a, b, key=len)
print(len(r), *r, sep='\n')
