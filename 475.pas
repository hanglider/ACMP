##
var t:=new list<integer>;
var f:text;
assign(f,'INPUT.TXT');
reset(f);
while not(seekeof(f)) do
  t.Add(readinteger(f));
t.Sort;
var r:=abs(t[0]-t[1]);
for var i:=2 to t.Count-1 do
  if r<> abs(t[i]-t[i-1]) then begin
    print('No');
    halt(0)
  end;
  print('Yes');
close(f)