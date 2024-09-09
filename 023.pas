var n,s,k:longint;
 begin
  {assign(input, 'input.txt'); reset(input); 
  assign(output, 'output.txt'); rewrite(output);
  }read(n);
  if n=1 then
   write (1)
 else
  begin
   s:=n+1;
   for k:=2 to n-1 do
    if n mod k=0 then s:=s+k;
   write (s);
  end;
end.