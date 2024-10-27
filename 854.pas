var tr,tk:integer;
    s:String;
begin
  Readln(tr,tk);
  readln(s);
  if s='fan' then Print(tr);
  if s='freeze' then Print(min(tr,tk));
  if s='heat' then Print(max(tk,tr));
  if s='auto' then Print(tk)  
end.