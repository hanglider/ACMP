var a: array [0..70] of int64;
i,n: byte;
begin
read(n);
a[1]:=1;
a[2]:=2;
a[3]:=4;
for i:=4 to n do
a[i]:=a[i-3]+a[i-2]+a[i-1];
writeln(a[n]);
end.