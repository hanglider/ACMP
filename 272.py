a = list(map(int, input().split()))
maxx = a[0]
minn = a[1]
for i in range(0,len(a),2):
    maxx = min(maxx, a[i])
for i in range(1,len(a), 2):
    minn = max(minn, a[i])
print(minn+maxx)