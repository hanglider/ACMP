t = [*map(int, open('input.txt').read().split())]
a, b, c, d = t[:4]
print(next((i // 2 - 1 for i in range(5, len(t), 2) if (t[i] - c)**2 + (t[i + 1] - d)**2 >= 4 * ((t[i] - a)**2 + (t[i + 1] - b)**2)), 'NO'))