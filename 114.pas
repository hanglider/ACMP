var
  n, k: int64;
  d, d0: array[1..1000] of integer;
 
begin
  read(n, k);
  d[1] := k - 1;
  d0[1] := 0;
  for var i := 2 to n do
  begin
    d[i] := (d[i - 1] + d0[i - 1]) * (k - 1);
    d0[i] := d[i - 1];
  end;
  write(d[n] + d0[n]);
end.