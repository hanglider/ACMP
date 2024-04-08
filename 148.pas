var a,b:integer;
begin
read(a,b);
while a*b > 0 do
  if a >= b then a := a mod b else b := b mod a;  
write(a+b); 
end.