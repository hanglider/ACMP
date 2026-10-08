data = open("INPUT.TXT").read().split()
n = int(data[0])
delta = [0] * 1002
for i in range(n):
    l, r, v = int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i])
    delta[l] += v
    delta[r] -= v
t_end = int(data[1 + 3 * n])
volume = 0
rate = 0
for t in range(min(t_end, 1000)):
    rate += delta[t]
    volume = max(0, volume + rate)
open("OUTPUT.TXT", "w").write(str(volume) + "\n")
