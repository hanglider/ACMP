var n:integer;
    a,c,b:array[1..10000] of int64;
    d:array[0..10000] of int64;
    k:int64;
begin
  readln(n);
  for var i:=1 to n do
   readln(a[i],b[i],c[i]);
  d[0]:=0;
  d[1]:=a[1];
  d[2]:=min(a[1]+a[2],b[1]);
  for var i:=3 to n do
  d[i]:=min(d[i-1]+a[i],min(d[i-2]+b[i-1],d[i-3]+c[i-2]));
  write(d[n])
end.