n, k = map(int, input().split())
s = input()
t = set()
for i in range(n-k+1):
    if not(s[i:i+k]) in t: 
        t |= {s[i:i+k]}
    else:
        print('YES')
        raise SystemExit
    print("NO")