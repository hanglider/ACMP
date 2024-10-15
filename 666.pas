##
var n := readlnint64;
var len := new int64[26];
len[0] := 1;
for var i := 1 to 25 do
  len[i] := len[i - 1] * 2 + 1;
var i := 25;
while n <> 1 do
begin
  if (n - 1) mod (len[i - 1]) <> 0 then n := (n - 1) mod (len[i - 1])
  else n := len[i - 1];
  i -= 1
end;
Print(char(ord('a') + i ))