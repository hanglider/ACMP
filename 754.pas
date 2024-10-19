program gg;
var a:array[1..3] of integer;
i,max,j:integer;
f:boolean;
begin
  f:=true;
  for i:=1 to 3 do
    read(a[i]);
  for i:=1 to 3 do
  if (a[i]<94) or (a[i]>727)
  then f:=false;
  max:=a[1];
  for j:=2 to 3 do
    if a[j]>max then max:=a[j];
  if f=true then write (max) else write ('Error');
end.