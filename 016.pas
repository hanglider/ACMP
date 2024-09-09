##
function rec(a, b: integer): integer;
begin
  if b=0 then result := 1
  else begin
    var ans: integer;
    for var i := 1 to a-1 do
      if b - i >= 0 then ans += rec(i, b - i);
    result := ans
  end;
end;
 
var n := readlninteger;
var c: integer;
for var i := 1 to n do
  c += rec(i, n - i);
c.Print