var a,b,c:integer;
begin
  readln(a,b,c);
  if (a+b>c) and (a+c>b) and (c+b>a) then Print('YES') else Print('NO')
end.