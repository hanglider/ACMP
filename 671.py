s = input()
l = len(s)
r = 2**l - 2
for i, c in enumerate(s):
    r += 2**(l - i - 1) * ((c > '4') + (c > '7'))
    if c not in '47':
        break
else:
    r += 1
print(r)
