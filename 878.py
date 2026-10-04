s = input().strip()
p = sorted(range(26), key=lambda i: s[i])
if all(s[j] >= chr(65 + i) for i, j in enumerate(p)):
    print('YES')
    print(*[i + 1 for i in p])
else:
    print('NO')
