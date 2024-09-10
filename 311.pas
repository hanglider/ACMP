var n:integer;
    c:biginteger;
    a:array of biginteger;
Function chet(a:integer):biginteger;
begin
  c:=1;
  for var i:=2 to a do
    c:=c*i;
  Result:=c
end;
begin
  n:=readlnInteger;
  a:=new BigInteger[n];
  for var i:=1 to n do
    a[i-1]:=chet(i);
  c:=a[0];
  for var i:=1 to n-1 do
    c+=a[i];
  Print(c)
end.