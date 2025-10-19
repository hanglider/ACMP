n=int(input())-1
x=0
while n:
    x^=(n%3>>1)   
    n//=3
print(x)
