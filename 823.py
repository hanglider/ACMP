n = int(input())
k=51
X = [k]*k
b = [0]*k
Y = 0
c = 1000000
for i in range(n):
	x, y = map(int, input().split())
	X[y] = min(X[y], x)
	b[y] = max(b[y], x)
	Y = max(Y, y)
t = Y + 2
w = [[c]*t for i in range(k)]
for y in range(1, t):
	for x in range(1,k):
		if y == 1:
			w[x][y] = x - 1
		else:
			for p in range(1, k):
				if b[y-1] == 0:
					w[x][y] = min(w[x][y], w[p][y - 1] + abs(x - p) + 1)
				else:
					w[x][y] = min(w[x][y], w[p][y - 1] + 1 + min(
						abs(p - b[y-1]) + (b[y-1] - X[y-1]) + abs(x - X[y-1]), 
						abs(p - X[y-1]) + (b[y-1] - X[y-1]) + abs(x - b[y-1])
						))
s = c
for i in range(1,k):
	s = min(s, w[i][Y+1])
print(s-1)	