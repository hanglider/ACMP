var x,x1,y,y1:integer;
begin
  read(x,y,x1,y1);
  x:=x1-x;
  x:=x*x;
  y:=y1-y;
  y:=y*y;
  Print(sqrt(x+y))
end.