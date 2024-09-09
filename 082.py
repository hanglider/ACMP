import math
from heapq import merge
const = 1e9.__trunc__()
def ans_print():
    print('ans: ', end='')
    return 0
def sort_merge(list1,list2):
    return sorted(list1+list2)
def bp_l(x):
    l = -1
    r = n  
    while r > l + 1:
        mid = (r+l)//2
    if  a[mid] > x:
        r = mid
    else:
        l = mid
    return l
def fib(i):
    k = math.sqrt(5)
    a = math.pow(((1+k)/2),t)
    b = math.pow(((1-k)/2),t)
    y = (a-b) / k
    return y
n, j = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))
c = list(set(a) & set(t))
c.sort()
if len(c) != 0:
    for i in range(len(c)):
        print(c[i], end=' ')