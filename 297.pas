var s:String;
    gh:integer;
begin
  s:=readlnstring;
  for var i:=1 to s.Length do
    if (s[i]='6') or (s[i]='9') or (s[i]='0') then inc(gh) else if s[i]='8' then inc(gh,2);
  gh.Print
end.