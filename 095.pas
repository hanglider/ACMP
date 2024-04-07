var s:string;
i,j,x,code,c:integer;
begin
read(s);
while length(s)>1 do
     begin
     for i:=1 to length(s) do
         begin
         val(s[i],x,code);
         c:=c+x;
         end;
     inc(j);
     Str(c,s);
     c:=0;
     end;
writeln(s,' ',j);
end.