var sum,mult,n,k:integer;
f1,f2:text;
begin
assign(f1,'input.txt');
assign(f2,'output.txt');
rewrite(f2);
reset(f1);
read(f1,n,k);
sum:=0; mult:=1;
while (n>0) do
begin
    sum := sum + n mod k;
    mult := mult * (n mod k);
    n := n div k;
end;
write(f2,mult-sum);
close(f1);
close(f2);
end.