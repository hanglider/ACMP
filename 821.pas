type mass = array [0..21,0..21] of integer;
     mas = array [1..4] of integer;
var t:mass;
    s,sb:mas;
    st:string;
    n,i,j,l,sch,f:integer;
begin
s[1]:=-1; s[2]:=0; s[3]:=1; s[4]:=0;
sb[1]:=0; sb[2]:=-1; sb[3]:=0; sb[4]:=1;

readln(n);

for i:=0 to n+1 do begin
 t[i,0]:=-1;
 t[i,n+1]:=-1;
end;

for j:=1 to n+1 do begin
 t[0,j]:=-1;
 t[n+1,j]:=-1;
end;

for i:=1 to n do
 for j:=1 to n do begin
  inc(sch);
  t[i,j]:=sch;
 end;
t[i,j]:=0;
readln(st);

while (l<length(st)) do begin
 inc(l);
if st[l]='U'
then sch:=1;
if st[l]='L'
then sch:=2;
if st[l]='D'
then sch:=3;
if st[l]='R'
then sch:=4;

if t[i+s[sch],j+sb[sch]]<>-1
then begin
 t[i,j]:=t[i+s[sch],j+sb[sch]];
 t[i+s[sch],j+sb[sch]]:=0;
 inc(i,s[sch]);
 inc(j,sb[sch]);
end
else begin
 f:=1;
 break;
end;
end;

if f=1
then writeln('ERROR',' ',l)
else begin
 for i:=1 to n do begin
  for j:=1 to n do
   write(t[i,j],' ');
  writeln;
 end;
end;
end.