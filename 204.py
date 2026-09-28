s = input()
p = [0]
for c in s[1:]:
    k = p[-1]
    while k and s[k] != c:
        k = p[k - 1]
    p += [k + (s[k] == c)]
print(len(s) - p[-1])
