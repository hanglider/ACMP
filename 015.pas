var 
i,j,n,s:integer;
a:array [1..100,1..100] of 0..1;
begin
read(n);
for i:=1 to n do
    for j:=1 to n do
       read(A[i,j]);
for i:=2 to n do
    for j:=1 to i-1 do
       if A[i,j]=1 then s:=s+1;
writeln(s);
end.