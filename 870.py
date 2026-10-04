import re
o = r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
for s in open(0).read().splitlines():
    m = re.fullmatch(r'(http://)?((%s\.){3}%s|(\w+\.)+[a-zA-Z]{2,3}|\w+)(:(0|[1-9]\d{0,4}))?(/(\w+/)*(\w+(\.\w+)*)?)?' % (o, o), s)
    print('YES' if m and int(m[8] or 0) < 65536 else 'NO')
