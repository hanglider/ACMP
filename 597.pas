var r1,r2,r3,n,i:integer; 
begin 
assign(input, 'input.txt'); reset(input); 
assign(output, 'output.txt'); rewrite(output); 
read(r1,r2,r3); 
for i:=1 to 1 do 
if r1>=r2+r3 
then write('YES') 
else write('NO'); 
end. 