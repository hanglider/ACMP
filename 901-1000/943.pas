var a:array[,] of integer;
    n,m,x,y:integer;
begin
  readln(n,m,x,y);
  var k:integer;
  a:=new integer[n,m];
  for var i:=0 to n-1 do    
    for var j:=0 to m-1 do
    begin
      if i mod 2 = 0 then a[i,j]:=k
      else a[i,m-j-1]:=k; 
      inc(k);
    end;
  Print(a[x-1,y-1])
end.