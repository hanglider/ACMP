begin
  var n, a, b, L, c, d, L1: integer;
  Read(n, c);
  L := 60001;
  loop n - 1 do
  begin
    Read(d);
    L1 := d - c;
    if L1 = 1 then
    begin
      Print(c, d);
      exit
    end;
    if L1 < L then
      (L, a, b) := (L1, c, d);
    c := d
  end;
  Print(a, b)
end.