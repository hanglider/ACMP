##
var (n,k):=readlninteger2;
var a:=readarrint64(n);
readln;
var t:=readarrint64(k);
var res:= new List <string>;
for var i:=0 to t.High do begin
  if a.BinarySearch(t[i]) >= 0 then res.add('YES')
  else res.add('NO')
end;
for var i:=0 to res.Count-1 do
  print(res[i])