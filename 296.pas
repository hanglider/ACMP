label m1;
var n,l,k:integer;
begin
  readln(n);
  var t,f,kol:integer;
  f:=n div 5;
  while n>0 do
  begin   
    t:=n - f*5;
    if t mod 3 = 0 then begin
      inc(kol,t div 3);
      Print(f, kol);
      halt(0);
    end else dec(f)
 end;
 Print(k,l)
end.