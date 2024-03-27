##
var s:=readlnstring;
var ans:integer;
for var i:=1 to s.Length-4 do
begin
  var s1:=copy(s,i,5);
  if (s1='>>-->') or (s1='<--<<') then ans+=1;
end;
ans.Print