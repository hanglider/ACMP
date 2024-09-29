##
function f(n:integer):integer;
begin
  if n=1 then f:=1 else
  if n=0 then f:=0 else  
  if n mod 2 = 0 then f:=f(n div 2)
  else f:=f((n-1) div 2) + f((n-1) div 2+1)
end;
print(f(readinteger))