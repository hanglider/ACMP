n = int(input())
a = ['A','B', 'C', 'E', 'H', 'K', 'M','O', 'P', 'T', 'X', 'Y']
digit = ['0','1','2','3','4','5','6','7','8','9']
for i in range(n):	
	s = str(input())
	if s == '':
		print('No')
		continue
	if len(s) != 6:
		print('No')
		continue
	if (s[0] in a) & (s[1] in digit) & (s[2] in digit) & (s[3] in digit) & (s[4] in a) & (s[5] in a) & (len(s) == 6):
		print('Yes')
	else:
		print('No')