##
var c:=0bi;
var n:=readlninteger;
var a1:= n div 4;
if (n<4) then print('0')
else begin
  for var i:=1 to a1 do
    for var j:=i to ((n-i) div 3) do
      c+=(n-i-j) div 2-j+1;
  c.Print
end