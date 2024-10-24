var n:integer;
    a:array of integer;
    c:biginteger;
begin
  n:=readinteger;
  a:=readarrinteger(n);
  c:=a[0];
  for var i:=1 to n-1 do
    c+=a[i]-1;
  Print(c);
end.