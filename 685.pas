var a,b:array of integer;
begin
  a:=ReadArrInteger(3);
  b:=ReadArrInteger(3);
  sort(a);
  sort(b);
  Print(a[0]*b[0]+a[1]*b[1]+a[2]*b[2])
end.