n, m = map(int, input().split())
d = {}
mmin = float('inf')
name = ""
for _ in range(n):
    s = input()
    a = list(map(int, input().split()))
    t = sum(a)
    if t < mmin:
        mmin = t 
        name = s
print(name)