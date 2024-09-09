##
var s:=readstring;
var n:=s.tobiginteger;
var g:='1'+'0'*((s.Length+1) div 2);
var a:=g.ToBigInteger;
var k:=a-1;
while k<a do begin
  a:=k;
  k:=(a + n div a) div 2
end;
a.Print