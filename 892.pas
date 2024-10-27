begin
  var n:=readinteger;
  if n<=0 then begin Print('Error'); halt(0) end;
  if n>12 then begin Print('Error'); halt(0) end;
  if (n<3) or (n>11) then begin Print('Winter'); halt(0) end;
  if (n>=3) and (n<6) then begin Print('Spring'); halt(0) end;
  if (n>=6) and (n<9) then begin Print('Summer'); halt(0) end;
  Print('Autumn')
end.