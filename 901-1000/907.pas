var
  w, h, r: int64;

function solve: boolean;
var rr:int64;
begin
  rr:= r*2;
  if (w >= rr) and (h >= rr) then solve := true;
end;

begin
  readln(w, h, r);
  if solve then write('YES') else write('NO')
end.