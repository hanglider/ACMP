##
var d:=new BigInteger[500,51];
d[0,0]:=1;
for var j:=0 to 49 do
  for var i:=0 to 499 do
    for var g:=0 to 9 do
      if i+g<500 then d[i+g,j+1]+=d[i,j];
var n:=readint64;
var с:=1bi;
for var i:=1 to (n div 2 * 9) + 1 do
begin
  var v:=d[i,n div 2];
  с+=v*v
end;
с.Print