var a,b,c,maxln:string; 
q:char; 
max: longint; 
begin
Read(q); 
a:=''; 
b:=''; 
c:=''; 
While q<>' ' do
begin
a:=a+q; 
Read(q); 
end; 
 
Read(q); 
While q<>' ' do
begin
b:=b+q; 
Read(q); 
end; 
 
Read(q); 
While not eoln do
begin
c:=c+q; 
Read(q); 
end; 
c:=c+q; 
if length(a)>length(b) then maxln:=a 
else if length(a)<length(b) then maxln:=b 
else if a>b then maxln:=a 
else maxln:=b; 
if length(c)>length(maxln) then maxln:=c 
else if (length(c)=length(maxln)) and (c>maxln) then maxln:=c; 
 
 
Writeln(maxln); 
end.