n = int(input())
h = [1]
i = j = k = 0
while len(h) < n:
    a, b, c = h[i] * 2, h[j] * 3, h[k] * 5
    m = min(a, b, c)
    h.append(m)
    if m == a:
        i += 1
    if m == b:
        j += 1
    if m == c:
        k += 1
print(h[n - 1])
