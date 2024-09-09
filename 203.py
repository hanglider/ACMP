ss = str(input())
pp = str(input())
s = ss.lower()
p = pp.lower()
tp = 0
ts = 0
for i in s:
    ts += ord(i)
for i in p:
    tp += ord(i)
if tp != ts:
    print(-1)
else:
    p = p*2
    t = p.find(s)
    print(t)