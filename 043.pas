var s:string;
i,x,max:integer;
begin
   x:=0;
   max:=x;
   read(s);
   for i:=1 to length(s) do
   begin
   if s[i]='0'
   then inc(x)
   else x:=0;
   if x>max
   then max:=x;
   end;
   write(max);
end.