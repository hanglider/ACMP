def sieve(n):
    pr = list(range(n + 1))
    pr[1] = 0
    i = 2
    while i * i <= n:
        if pr[i]:
            j = i * i
            while j <= n:
                pr[j] = 0
                j += i
        i += 1
    return pr
a = sieve(1000)
prost_chisla = []
for i in range(len(a)):
    if a[i] != 0:
        prost_chisla.append(a[i])
#print(prost_chisla)
n = int(input())
const = 1e4.__trunc__()
ans1 = const - 1
ans2 = const 
for i in range(len(prost_chisla)):
    for j in range(i, len(prost_chisla)):
        if prost_chisla[i] + prost_chisla[j] == n:
            k = min(prost_chisla[i],prost_chisla[j])
            if k < ans1:
                ans1 = min(prost_chisla[i], prost_chisla[j])
                ans2 = max(prost_chisla[i], prost_chisla[j])
print(ans1, ans2)