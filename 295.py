import string 
a = string.ascii_uppercase
s = list(input())
t = input()
y = ""
for i in range(52):
    for i in range(len(s)):
        s[i] = a[(a.index(s[i]) + 1) % 26]
    r = "".join(s)
    if t in r:
        y = r 
if y != "":
    print(y)
else:
    print("IMPOSSIBLE")