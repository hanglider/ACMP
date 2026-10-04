for _ in range(int(input())):
    a, b, c = sorted(map(int, input().split()))
    print(["No", "Yes"][(a ^ b | b ^ c) & 1 > (b < 1 < c)])
