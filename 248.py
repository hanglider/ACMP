import re


def f(m):
    w = m[0]
    l = w.lower()
    if l in ('a', 'an', 'the'):
        return ''
    r = ''
    for c in re.sub('c(?=[ie])', 's', l).replace('ck', 'k').replace('c', 'k'):
        r += c
        while len(r) > 1 and r[-1] == r[-2]:
            r = r[:-2] + {'e': 'i', 'o': 'u'}.get(c, c)
            c = r[-1]
    if len(r) > 1 and r[-1] == 'e':
        r = r[:-1]
    return r.capitalize() if w[0] < 'a' else r


print(' '.join(re.sub('[a-zA-Z]+', f, input()).split()))
