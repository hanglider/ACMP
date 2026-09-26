s = ''.join(open('input.txt').read().split())
t = s[:3], s[3:6], s[6:], s[::3], s[1::3], s[2::3], s[::4], s[2:7:2]
print('Win' if 'XXX' in t else 'Lose' if 'OOO' in t else 'Draw')