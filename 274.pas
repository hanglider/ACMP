var a,b:longint;
c,d:array [0..9] of byte;
i,k:byte;
t:boolean;
begin
assign(input,'input.txt'); reset(input);
assign(output,'output.txt'); rewrite(output);
read(k);
while k>0 do
begin
k:=k-1;
read(a,b);
for i:=0 to 9 do begin c[i]:=0; d[i]:=0 end;
while a>0 do
begin
c[a mod 10]:=1;
a:=a div 10
end;
while b>0 do
begin
d[b mod 10]:=1;
b:=b div 10
end;
t:=true;
for i:=0 to 9 do
t:=t and (c[i]=d[i]);
if t then write('YES')
else write('NO');
if k>0 then writeln
end
end.