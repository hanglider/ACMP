s = input()
l = 1
a = 1
r = 1
for i in s:
    if i == "1":
        l += 1
    else:
        l -= 1
    r = max(r, l)
    a = min(a, l)
print(r - a + 1)