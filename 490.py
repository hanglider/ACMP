from datetime import*
a, b = [datetime.strptime(input(), '%d.%m.%y') for _ in '12']
print((b - a).days)
