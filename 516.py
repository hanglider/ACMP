def P(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

n = input()
a = int(''.join(sorted(n)))
b = int(''.join(sorted(n, reverse=True)))
print("Yes" if P(a) and P(b) else "No")
