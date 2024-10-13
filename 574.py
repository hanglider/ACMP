from collections import Counter
def anagrams(str1, str2):
    return Counter(str1) == Counter(str2)
if anagrams(str(input()), str(input())):
    print(('YES'))
else:
    print('NO')