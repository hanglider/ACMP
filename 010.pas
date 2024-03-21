type mass=array[1..200] of integer;
var a,b,c,d,i,n:longint;
m:mass;
f:text;
begin
    read(a,b,c,d);
    n:=1;
    for i:=-100 to 100 do
    if (i*i*i)*a+i*i*b+c*i+d=0 then begin 
        m[n]:=i; 
        inc(n); 
    end;
    for i:=1 to n-1 do begin
        write(m[i]);
        write(' ');
    end;
end.