Program da; 
type mass=array[0..1002] of longint; 
var m:mass;
max,min,a,l,q,b,i,k,n:longint; 
Begin 
readln(n); 
read(m[1+n]); 
m[1]:=m[1+n]; 
read(m[2+n]); 
m[2]:=m[2+n]; 
for i:=3 to n do 
read(m[i]); 
max:=m[1]+m[2]+m[3]; 
for i:=2 to n+1 do 
Begin 
if m[i]+m[i-1]+m[i+1]>max 
then max:=m[i]+m[i-1]+m[i+1]; 
end; 
writeln(max); 
end.