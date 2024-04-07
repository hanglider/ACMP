var
  n, p: integer;
  a, b, c: biginteger;
  f: array[1..1000] of integer;
 
begin
  n := Readlninteger;
  c:=45;
  if n>1 then
  for var i:=2 to n do
    c:=c*45
    else c:=45;
  Print(c) 
end.