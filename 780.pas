var n,a,b,k:integer;
begin
  readln(n);  
  var fa:=true;
  var fb:=false;
  while k<>n do
  begin
    if fa then begin inc(a); fa:=false end else fa:=true;
    if fb then begin inc(b); fb:=false end else fb:=true;
    inc(k,a+b)
  end;
  Print(a+b);
end.