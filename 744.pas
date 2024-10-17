##
var s := readstring();
if s = '' then begin
  print('YES');
  halt(0)
end;
if s.Length < 2 then begin
  print('NO');
  halt(0)
end;
var f := true;
var x : char;
for var j := 0 to s.Length do begin
  x := s[1];
  s := s[2:s.Length+1];
  s += x;
  f := true;
  var q := new Stack<char>;
  for var i := 1 to s.Length do
  begin
    if (q.Count = 0) and ((s[i] = '}') or (s[i] = ')') or (s[i] = ']'))
    then begin f := false; break end;
    if (s[i] = '{') or (s[i] = '(') or (s[i] = '[') then q.Push(s[i]);
    if (s[i] = ']') and (q.Peek = '[') then q.Pop; 
    if (s[i] = ')') and (q.Peek = '(') then q.Pop; 
    if (s[i] = '}') and (q.Peek = '{') then q.Pop; 
  end;
  if q.Count <> 0 then f := false;
  if f then begin
    print('YES');
    halt(0)
  end;
  //s.Println;
end;
print('NO')
