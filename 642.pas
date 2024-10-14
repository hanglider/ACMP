var
  n, s: integer;
  a: array of integer;

begin
  readln(n, s);
  a := readarrinteger(n);
  sort(a);
  var k: integer;
  for var i := 0 to n - 1 do
    if s - a[i] >= 0 then begin
      inc(k);
      s -= a[i];
    end else break;
  Print(k)
end.