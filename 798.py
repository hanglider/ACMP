m, n, i, j, c = map(int, open('input.txt').read().split())
print(m * n % 2 and ['black', 'white'][c ^ (i + j) % 2] or 'equal')