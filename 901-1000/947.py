X = float(input())
i = 2
start = float(1/i)
j = 1
while X >= start:
    i+=1
    start+=float(1/i)
    j+=1
print(j, "card(s)")