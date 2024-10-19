begin
  var n := ReadInteger;
  var (V, L) := ReadlnReal2;
  var (S, t) := (60 * L / V, 0);
  loop n do
  begin
    var (p, ti) := ReadInteger2;  
    t += ti
  end;
  Write(S + t:0:2)
end.