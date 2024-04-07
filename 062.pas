var
  a: array[1..8, 1..8] of string;
  f: boolean;
  s: string;
  x: char;
  Y, h: integer;
 
begin
  f := true;
  for var i := 1 to 8 do
  begin
    for var j := 1 to 8 do
      if f then begin a[i, j] := 'BLACK'; f := false end else begin a[i, j] := 'WHITE'; f := true end;
    if f then f := false else f := true
  end;
  read(s);
  x := s[1]; 
  val(s[2], y, h);
  if x = 'A' then Print(a[1, y]);
  if x = 'B' then Print(a[2, y]);
  if x = 'C' then Print(a[3, y]);
  if x = 'D' then Print(a[4, y]);
  if x = 'E' then Print(a[5, y]);
  if x = 'F' then Print(a[6, y]);
  if x = 'G' then Print(a[7, y]);
  if x = 'H' then Print(a[8, y]);
end.