def f(s):
    ans = 0
    for i in s:
        ans += int(i)
    return ans
 
def sqr(a, b):
    s1, s2 = 11, 11
    while s1 >= 10: 
        s1 = f(a)
        a = str(s1)
    while s2 >= 10:
        s2 = f(b)
        b = str(s2)
    if s1 == s2:
        return True
    else:
        return False
 
def solve():
    s = input()
    for i in range(1, len(s)):
        #print(s[:i], s[i:])
        if sqr(s[:i], s[i:]):
            print("YES")
            return None
    print("NO")
     
t = 1
#t = int(input())
while t:
    solve()
    t -= 1