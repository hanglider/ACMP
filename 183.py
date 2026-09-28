k, p = map(int, input().split())
e = [0, 1]
for m in range(2, k // 2 + 1):
    e += [(e[-1] + e[m // 2]) % p]
print(e[k // 2] % p)
