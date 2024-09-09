var a:array of integer;
begin
  var n:integer;
  readln(n);
  a:=ReadArrInteger(n);
  for var i:=n-1 downto 0 do
    Print(a[i])
end.