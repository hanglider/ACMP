import re
q, t = open(0).read().split('\n', 1)
print(re.sub('(?=' + r'\s+'.join(q.split()) + ')', '@', t, flags=re.I), end='')
