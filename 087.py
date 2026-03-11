a=[]
while 1:
    s=input()
    if s=='ENDOFINPUT':
        break
    a.append(s)

b=set(a)
c=0

for s in a:
    for i in range(1,len(s)):
        if s[:i] in b and s[i:] in b:
            c+=1
            break

print(c)