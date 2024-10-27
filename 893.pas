var n:int64;
begin
  readln(n);
  if (n=1) or (n=2) then begin
    Print(n);
    halt(0)
  end;
  Print(n*(n-1)*(n-2))
end.