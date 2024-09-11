var
n,i,a,k:integer;
s:array[0..1000]of longint;
t:array[1..1000]of integer;
begin
assign(input,'input.txt'); reset(input);
assign(output,'output.txt'); rewrite(output);
read(n); s[0]:=0;
read(a); s[1]:=a;
for i:=2 to n do
begin
read(a);
if s[i-2]<s[i-1] then s[i]:=a+s[i-1] else s[i]:=a+s[i-2]
end;
writeln(s[n]);
k:=1; t[k]:=n;
while n>1 do
begin
if s[n-2]<s[n-1] then n:=n-1 else n:=n-2;
if n>0 then begin k:=k+1; t[k]:=n end
end;
for i:=k downto 1 do write(t[i],' ')
end.