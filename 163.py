s = input().replace("=", "==")
print(*[x for x in range(-9, 19) if eval(s.replace("x", str(x)))])
