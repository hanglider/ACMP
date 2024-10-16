type mass = array [1..9,1..4] of integer;
var a,b,s:string;
    i,c,x,n,code:integer;
    t:mass;
begin
readln(s);
 a:=copy(s,1,pos(' ',s)-1);
 b:=copy(s,pos(' ',s)+1,length(s));
 val(b[length(b)],x,code);
 val(a[length(a)],c,code);
 n:=x mod 4;
 if n=0
 then n:=4;

t[1,1]:=1; t[1,2]:=1; t[1,3]:=1; t[1,4]:=1;
t[2,1]:=2; t[2,2]:=4; t[2,3]:=8; t[2,4]:=6;
t[3,1]:=3; t[3,2]:=9; t[3,3]:=7; t[3,4]:=1;
t[4,1]:=4; t[4,2]:=6; t[4,3]:=4; t[4,4]:=6;
t[5,1]:=5; t[5,2]:=5; t[5,3]:=5; t[5,4]:=5;
t[6,1]:=6; t[6,2]:=6; t[6,3]:=6; t[6,4]:=6;
t[7,1]:=7; t[7,2]:=9; t[7,3]:=3; t[7,4]:=1;
t[8,1]:=8; t[8,2]:=4; t[8,3]:=2; t[8,4]:=6;
t[9,1]:=9; t[9,2]:=1; t[9,3]:=9; t[9,4]:=1;

 writeln(t[c,n]);
end.