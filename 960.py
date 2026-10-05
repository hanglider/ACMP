import sys

s = sys.stdin.read().strip()
a = ab = abc = 0
for ch in s:
    if ch == 'a':
        a += 1
    elif ch == 'b':
        ab += a
    elif ch == 'c':
        abc += ab
print(abc)
