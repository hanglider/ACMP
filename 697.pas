var l,a,b,c:integer;
begin
  readln(a,b,c);
  l := b*c*2+a*c*2;
  if l mod 16 <>0 then Print(l div 16 + 1) else Print(l div 16)
end.