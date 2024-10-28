var a:array[1..4,1..4] of char;
Procedure proverka(i,j,x:integer; c:char);
begin
  if (a[x+1,i]=a[x+1,j]) and (c=a[x+1,i]) then begin
    Print('No');
    halt(0)
  end;
end;
begin
  for var i:=1 to 4 do
  begin    
    for var j:=1 to 4 do
     read(a[i,j]);
    readln;
  end;
  for var i:=1 to 3 do
    for var j:=2 to 4 do
      if a[i,j-1]=a[i,j] then proverka(j-1,j,i,a[i,j]);
  Print('Yes')
end.