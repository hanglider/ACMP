s=list(input())
t=input()
o=[]
for i in range(len(s)):
    if s[i]!=t[i]:
        j=i
        while s[j]!=t[i]:j+=1
        s[i:j+1]=s[i:j+1][::-1]
        o+=(i+1,j+1),
print(len(o))
for l,r in o:print(l,r)
