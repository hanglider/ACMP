s = sorted(input())
z = s.count('0')
print(s[z] + '0' * z + ''.join(s[z + 1:]), ''.join(s[::-1]))
