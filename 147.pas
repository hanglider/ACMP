var i,n,a,b,y,x:longint;
begin
   read(n);
   a:=0;
   b:=1;
   for i:=2 to n do
   begin
      b:=a+b;
      a:=b-a
   end;
   if n<2 then write(n) else write(b);
end.