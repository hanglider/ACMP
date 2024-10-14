##
var b:=1;
var a:=1;
var x:integer;
var t:=readinteger;
for var i:=2 to t do
begin
  var y:=b;
  b:=(a+b)  mod 10;
  a:=y
end;
Print(b mod 10)
