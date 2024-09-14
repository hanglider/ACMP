k = 1
s = 0
input_str = input()  
for c in input_str:
    s += k * (ord(c) - 48)  
    k = -k  
if s % 11 == 0:
    print("YES")
else:
    print("NO")
