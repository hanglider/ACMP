var s:string;
begin
  s:=readstring;
  for var i:=1 to length(s) do
    if s[i]='0' then begin Print('NO'); halt(0) end;
  Print('YES');
end.