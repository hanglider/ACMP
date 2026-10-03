a, b = input().lower().split()
print(["No", "Yes"][sorted(a) == sorted(b)])
