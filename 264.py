t = open('input.txt').read().split()[1:]
print(max(map(len, ''.join('01'[int(x) > 0] for x in t).split('0'))))