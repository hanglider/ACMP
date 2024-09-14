##
function cor(a, b: char): boolean;
begin
  var num := 10 * (ord(a) - ord('0')) + ord(b) - ord('0');
  if (num >= 10) and (num <= 33) then result := true else result := false
end;
var s := readlnstring;
var a := new BigInteger[s.Length+1];
a[0] := 1;
a[1] := 1;
for var i := 2 to a.High do
begin
  a[i] += a[i - 1];
  if cor(s[i - 1], s[i]) then a[i] += a[i - 2]
end;
a.Last.Print