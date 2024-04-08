var a, n:integer;
function solve:integer;
var zero, one:integer;
begin
  readln(n);
  for var i:=1 to n do
  begin
    readln(a);
    if a=0 then inc(zero) else inc(one)
  end;
  if zero<one then solve:=zero else solve:=one;
end; 
begin
  write(solve)
end.