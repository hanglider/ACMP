import re
s = input()
for p in range(len(s)):
    for c in "<>/a":
        t = s[:p] + c + s[p + 1:]
        if re.fullmatch("(</?[a-z]+>)*", t):
            k = re.findall("<(/?)([a-z]+)>", t)
            m = {}
            q = []
            for i, (x, y) in enumerate(k):
                if x:
                    if not q:
                        break
                    j = q.pop()
                    m[i] = j
                    m[j] = i
                else:
                    q += [i]
            else:
                if q:
                    continue
                if c > ">":
                    i = t[:p].count("<") - 1
                    w = k[m[i]][1]
                    o = p - t.rfind("<", 0, p) - 1 - len(k[i][0])
                    if len(w) - len(k[i][1]):
                        continue
                    t = t[:p] + w[o] + t[p + 1:]
                    k = re.findall("<(/?)([a-z]+)>", t)
                if t != s and all(k[i][1] == k[m[i]][1] for i in m):
                    print(t)
                    exit()
