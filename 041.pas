var
i,n:longint; 
buf,X:extended; 
a:array[1..1000000]of extended; 
 
procedure Sort(L,R:Longint); 
var
 
j:longint; 
 
begin
i:=L; j:=R; X:=a[(i+j)shr 1]; 
repeat
while a[i]<X do inc(i); 
while a[j]>X do dec(j); 
if i<=j then begin
buf:=a[i]; a[i]:=a[j]; a[j]:=buf; 
inc(i); dec(j); 
end; 
until i>j; 
if i<R then Sort(i,R); 
if j>L then Sort(L,j); 
end; 
 
begin
assign(input,'input.txt'); 
assign(output,'output.txt'); 
reset(input); 
rewrite(output); 
read(input,n); 
for i:=1 to n do read(input,a[i]); 
sort(1,n); 
for i:=1 to n do write(output,a[i]:0:0,' '); 
close(output); 
close(input); 
end.