import re
s = open(0, encoding='latin1').read().replace('\r', '').split('\n')
t = '\n'.join(s[1:int(s[0]) + 1])
k = []
m = {}
for i, c in enumerate(t):
    if c == '{':
        k += [i]
    if c == '}':
        m[k.pop()] = i


def f(i, e):
    o = ''
    while i < len(t) and t[i] != '}':
        if t[i] == '{':
            o += '{' + f(i + 1, e) + '}'
            i = m[i] + 1
            continue
        g = re.match(r'#(#?)([a-z]+) ?', t[i:])
        if not g:
            o += t[i]
            i += 1
            continue
        w = g[2]
        i += g.end()
        if g[1]:
            if w in e:
                o += f(*e[w])
        elif w == 'rep':
            j = t.find(' ', i)
            o += f(j + 2, e) * int(t[i:j])
            i = m[j + 1] + 1
        else:
            e = {**e, w: (i + 1, e)}
            i = m[i] + 1
    return o


open(1, 'w', encoding='latin1').write(f(0, {}) + '\n')
