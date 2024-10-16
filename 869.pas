type mass = array [1..15000] of integer;
var n,d,max,t:longint;
    m:mass;
    i,j,ans:integer;

procedure QuickSort( L, R : Integer );
var i,j,x,y : integer;
begin
  i := l; j := r;
  x := m[(l+r) div 2];
  repeat
    while (m[i] < x) do inc(i);
    while (x < m[j]) do dec(j);
    if ( i <= j ) then
    begin
      y:=m[i]; m[i]:=m[j]; m[j]:=y;
      inc(i); dec(j);
    end;
  until (i > j);
  if (l < j) then QuickSort(l,j);
  if (i < r) then QuickSort(i,r);
end;


begin
readln(n,d);
for i:=1 to n do
 read(m[i]);
 QuickSort(1,n);

 i:=1;
 j:=n;
 while (i<j) do begin
  if (m[i]+m[j])<=d then inc(i);
  inc(ans);
  dec(j);
 end;
 if(i=j) then inc(ans);
 writeln(ans);

end.
