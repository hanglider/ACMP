x, y = map(int, open('input.txt').read().split())
print(x - y and 1 or 2 * (x > 1))