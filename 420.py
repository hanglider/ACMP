s = open('input.txt').read().strip()
n = len(s)
i = 0
ok = True
prev = None
while i < n and ok:
    if not s[i].isupper():
        ok = False
        break
    j = i + 1
    if j < n and s[j].islower():
        j += 1
    el = s[i:j]
    k = j
    while k < n and s[k].isdigit():
        k += 1
    if k > j:
        num = s[j:k]
        if num[0] == '0' or int(num) < 2:
            ok = False
            break
    if el == prev:
        ok = False
        break
    prev = el
    i = k
print("YES" if ok else "NO")
