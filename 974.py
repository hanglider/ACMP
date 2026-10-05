# Brute force shows: the position is losing for the player to move
# exactly when (a+1) xor (b+1) xor (c+1) == 0.
result = []
for line in open("INPUT.TXT"):
    nums = line.split()
    if len(nums) < 3:
        continue
    a, b, c = map(int, nums)
    if a == 0 and b == 0 and c == 0:
        break
    if (a + 1) ^ (b + 1) ^ (c + 1) == 0:
        result.append("Bob wins the game.")
    else:
        result.append("Alice wins the game.")
open("OUTPUT.TXT", "w").write("\n".join(result) + "\n")
