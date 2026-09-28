n, k = map(int, input().split())
s = ""
for d in range(9, 1, -1):
    while k % d < 1:
        s = str(d) + s
        k //= d
print("YNEOS"[k > 1 or int(s or 1) > n::2])
