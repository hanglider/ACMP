s = open(0, 'rb').read().split(b'\n')
k, n = map(int, s[0].split())
t = [x.strip() for x in s[1:n + 1]]
if max(map(len, t)) > k:
    print("Impossible.")
else:
    open(1, 'wb').write(b'\n'.join((b' ' * ((k - len(x)) // 2) + x).ljust(k) for x in t))
