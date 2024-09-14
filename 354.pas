var i,n:integer;
begin
  read(n);
  i:=2;
  while(i <= sqrt(n)) do
  
  if (n mod i=0) then begin
      write(i);
      n:=n div i;
      if(n>1) then write('*')
    end
    else inc(i);
  if(n>1) then write(n);
 
end.