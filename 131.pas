var n,max,v,s,num:integer;
begin
  readln(n);
  for var i:=1 to n do
  begin
  readln(v,s);
    if (s=1) and (v>max) then begin
      max:=v;
      num:=i
    end
  end;
  if num<>0 then Print(num) else Print('-1')
end.