p = 1
m = '021301320321'
for c in input():
    p = int(m[ord(c) % 65 * 4 + p])
print(p)
