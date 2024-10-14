var n,s,d:longint;
begin
  read(n);
  begin
  s := 0;
  d:=n;
  while(n>0) do
  begin
    s := s + n mod 2;
    n := n div 2;
  end;
  end;
  write(d+s);
end.