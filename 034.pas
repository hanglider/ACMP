##
var a := new HashSet <string>;
var (n,k) := readlninteger2;
var s := readstring;
for var i := 1 to s.Length - k + 1  do begin
  var cur := s[i:i+k];
  if cur in a then begin
    'YES'.Print;
    halt(0)
  end else a.Add(cur)
end;
'NO'.Print