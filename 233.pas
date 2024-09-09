var f1,f2:text;
a:array [0..1000] of integer;
i,s:integer;
flag:boolean;
begin
assign(f1,'input.txt');
assign(f2,'output.txt');
reset(f1);
rewrite(f2);
read(f1,a[0]);
flag:=false;
for i:=1 to a[0] do
    read(f1,a[i]);
for i:=1 to a[0] do
    if(a[i]<=437) then begin
                       flag:=true;
                       s:=i;
                       break;
                       end;
if(flag) then write(f2,'Crash ',i) else write(f2,'No crash');
close(f1);
close(f2);
end.