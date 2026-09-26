t = open('input.txt').read().splitlines()
print(t[0] + ': ' + ', '.join(sorted(t[1:4])))