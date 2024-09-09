from fractions import Fraction
 
def checkio1(data):
    ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    hunds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    thous = ["","M","MM","MMM","MMMM"]
     
    t = thous[data // 1000]
    h = hunds[data // 100 % 10]
    te = tens[data // 10 % 10]
    o =  ones[data % 10]
     
    return t+h+te+o
 
integers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
  
def roman_to_arabic(roman):
    result = 0
    for i, c in enumerate(roman):
        if i+1<len(roman) and integers[roman[i]] < integers[roman[i+1]]:
            result-=integers[roman[i]]
        else:
            result+=integers[roman[i]]
    return str(result)
 
 
st = ["I", "V", "X", "L", "C", "D", "M", "/"]
s = input()
for i in s:
    if not i in st:
        print("ERROR")
        exit()
n = s.find("/")
a = s[:n]
b = s[n+1:]
ach = roman_to_arabic(a)
bch = roman_to_arabic(b)
t = Fraction(int(ach), int(bch))
s = str(t)
n = s.find("/")
if n == -1:
    print(checkio1(int(s)))
else:
    a = s[:n]
    b = s[n+1:]
    #print(a, b )
    print(checkio1(int(a))+"/"+checkio1(int(b)))