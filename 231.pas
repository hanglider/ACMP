program exp1; 
var f,t:text; 
a:string;d,l,chislo,c,i,k:integer; 
begin
assign(f,'input.txt'); 
assign(t,'output.txt'); 
reset(f);rewrite(t); 
read(f,a); 
k:=1;l:=1; 
while k<=length(a) do begin
val(a[k],c,d);chislo:=0; 
while d=0 do begin
chislo:=chislo*10+c; 
inc(k);val(a[k],c,d);end; 
if chislo=0
then chislo:=1; 
for i:=1 to chislo do
if l>39 then begin l:=1;writeln(t,a[k]);end
else begin inc(l);write(t,a[k]);end;inc(k);end; 
close(f);close(t);end.