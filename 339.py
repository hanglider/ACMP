from datetime import*
a, b = [date(*map(int, input().split('.')[::-1])) for _ in 'ab']
print((b - a).days + 1)
