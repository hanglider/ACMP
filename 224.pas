##
var n:=readlninteger;
var a:=readarrinteger(n);
var max_arr := new integer[3];
var min_arr := new integer[2];
for var i := 0 to 2 do
  max_arr[i] := -100000;
for var i := 0 to 1 do
  min_arr[i] := 1000000;
for var i := 0 to n-1 do begin
  if a[i] > max_arr[0] then begin
    max_arr[0] := a[i];
    max_arr.sort
  end;
  if a[i] < min_arr[1] then begin
    min_arr[1] := a[i];
    min_arr.Sort
  end;
end;
print(max(1bi * max_arr[0] * max_arr[2] * max_arr[1],1bi * max_arr[2] * min_arr[0] * min_arr[1]))