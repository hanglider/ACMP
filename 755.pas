var n,x,y,z:integer;
begin
  read(x,y,z);
  n:=x+y;
  if n>=z then write(n-z) else write('Impossible');
end.