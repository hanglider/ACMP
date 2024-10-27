import math
def solve():
    pi = math.pi
    s, r = map(float, input().split())
    print(((r*r*pi-s)/pi)**0.5)
t = 1
#t = int(input())
while t > 0:
    solve() 
    t -= 1