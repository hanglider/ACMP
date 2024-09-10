var n,m:integer;
    a:array of integer;
begin
  readln(n);
  a:=readarrinteger(n);
  readln;
  readln(m);
  var x,y:integer;
  for var i:=0 to m-1 do
  begin
    read(x,y);
    for var j:=x-1 to y-1 do
      Print(a[j]);
    readln;
  end;
end.