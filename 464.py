def reverse(s):
    if s == "0": return "1"
    if s == "1": return "2"
    if s == "2": return "0"

n = int(input())
st = [2**i for i in range(31)]
i = 0
while n > 1:
    p = len(st) - 1
    while n - st[p] <= 0:
        p -= 1
    n -= st[p]
    i += 1
t = "0"
for j in range(i):
    t = reverse(t)
print(t)