var c,h,o,x,y:int64;
begin
  readln(c,h,o);
  x:=c div 2;
  y:=h div 6;
  Print(min(min(x,y),o))
end.