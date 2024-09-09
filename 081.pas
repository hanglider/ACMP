var a:array of integer;
n:integer;
begin
  readln(n);
  a:=ReadArrInteger(n);
  sort(a);
  Print(a[0],a[n-1])
end.