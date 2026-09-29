s = list(map(int, input().split()))
k = sum(map(s.count, s))
k -= k < 6 > max(s) - min(s) + 1
print({25: "Impossible", 17: "Four of a Kind", 13: "Full House", 4: "Straight", 11: "Three of a Kind", 9: "Two Pairs", 7: "One Pair", 5: "Nothing"}[k])
