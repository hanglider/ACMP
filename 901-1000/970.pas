var a,b,c:int64;
begin
  readln(a,b,c);
  if a+c=b then begin Print('YES'); halt(0) end;
  if a+b=c then begin Print('YES'); halt(0) end;
  if b+c=a then begin Print('YES'); halt(0) end;
  Print('NO')
end.