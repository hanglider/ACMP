n = int(input())
a = list(map(int, input().split()))
k = int(input())
t = list(map(int, input().split()))
for i in range(k):
	a[t[i]-1] -= 1
for i in a:
	if i >= 0:
		print("no")
	else:
		print("yes")