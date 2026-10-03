a, b = input().split()
x = abs(ord(b[0]) - ord(a[0]))
y = int(b[1]) - int(a[1])
print("YES" if x <= y and (x + y) % 2 < 1 else "NO")
