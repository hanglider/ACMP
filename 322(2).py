string = input()
fib1, fib2 = 0, 1
for i in range(len(string) + 1):
    fib1, fib2 = fib2, fib1 + fib2
    if fib2 < len(string) + 1:
        print(string[fib2 - 1], end='')