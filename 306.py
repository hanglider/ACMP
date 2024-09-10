import queue
n = int(input())
q = queue.Queue()
 
for i in range(n):
    q.put(i) 
 
t = []
while q:
    t += [q.get()]      
    if q.empty(): break
    q.put(q.get())
 
for i, k in sorted({t[i]: "B" if i % 2 == 0 else "R" for i in range(n)}.items(), key = lambda x:x[0]):
    print(k, end='')