from fractions import Fraction

data = open("INPUT.TXT").read().split()
n = int(data[0])
bx, by = int(data[1]), int(data[2])
limit = Fraction(data[3]) ** 2
answer = "Yes"
for i in range(n):
    x = int(data[4 + 2 * i])
    y = int(data[5 + 2 * i])
    if (x - bx) ** 2 + (y - by) ** 2 <= limit:
        answer = str(i + 1)
        break
open("OUTPUT.TXT", "w").write(answer + "\n")
