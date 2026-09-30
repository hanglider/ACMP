n = int(input())
g = ['46', '68', '79', '48', '039', '', '017', '26', '13', '24']
c = [1] * 10
for _ in range(n - 1):
    c = [sum(c[int(j)] for j in g[i]) for i in range(10)]
print(sum(c) - c[0] - c[8])
