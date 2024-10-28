var a,b,c,d,max,min:biginteger;
begin
  c:=readbiginteger;
  max:=c*6;
  a:=c div 6;
  b:=c mod 6;
  if b=0 then min:=a;
  if b=5 then min:=2+a;
  if b=4 then min:=3+a;
  if b=3 then min:=4+a;
  if b=2 then min:=5+a;
  if b=1 then min:=6+a;
  Print(min,max)
end.
