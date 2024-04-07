var c:real;
begin
  loop 8 do c:=ReadReal-c;
  write(c=0?'DRAW':c<0?'1':'2')
end.