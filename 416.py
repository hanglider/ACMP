s = input()
for c in 'abcdefgh':
    for d in '12345678':
        if ((ord(c) - ord(s[0])) * (ord(d) - ord(s[1])))**2 == 4:
            print(c + d)
