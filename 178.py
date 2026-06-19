with open('input.txt', 'r') as f:
    data = f.read().split()

n = int(data[0])
a = [int(x) for x in data[1:n+1]]

cnt = {}
for x in a:
    cnt[x] = cnt.get(x, 0) + 1

max_c = -1
best_val = float('inf')

for x, c in cnt.items():
    if c > max_c or (c == max_c and x < best_val):
        max_c = c
        best_val = x

res = [x for x in a if x != best_val]
res.extend([best_val] * max_c)

print(*res)
