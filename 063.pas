var s,p,x,y,x1:integer;
begin
read(s,p);
for x:=1 to 30000 do
begin
  y:=s-x;
  x1:=x*y;
  if(x<=y) and (x1=p) then write(x,' ',y);
end;
end.