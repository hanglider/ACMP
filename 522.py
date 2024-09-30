m,n = map(int, input().split())
if set(list(map(int, input().split()))) != set(list(map(int, input().split()))):
    print(0)
else:
    print(1)