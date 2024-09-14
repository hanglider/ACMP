input()
a = list(map(int, input().split()))
a.sort()
s = 0
a = a[::-1]
for i, j, k in zip(a, a[1:], a[2:]):
    if i >= j + k:
        continue
    else:
        p = (i+j+k)/2
        s = max(s, abs((p*(p-i)*(p-j)*(p-k)))**(0.5))
 
print(f'{s:.3f}' if s > 0 else 0)