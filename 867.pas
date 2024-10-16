type mass = array [1..10000] of longint;
var t,nom,ans,ch:mass;
    d,i,j,n,max:longint;
Procedure Sort(l,r:longint);
var x,y,i,j,z:longint;
begin
 i:=l;
 j:=r;
 x:=t[(i+j) div 2];
 repeat
  while (t[i]<x) do inc(i);
  while (t[j]>x) do dec(j);
  if i<=j
  then begin
   y:=t[i];
   z:=nom[i];
   t[i]:=t[j];
   nom[i]:=nom[j];
   t[j]:=y;
   nom[j]:=z;
   inc(i);
   dec(j);
  end;
 until(i>j);
 if j>l then Sort(l,j);
 if r>i then Sort(i,r);
end;
Procedure Sort2(l,r:longint);
var x,y,i,j,z:longint;
begin
 i:=l;
 j:=r;
 x:=nom[(i+j) div 2];
 repeat
  while (nom[i]<x) do inc(i);
  while (nom[j]>x) do dec(j);
  if i<=j
  then begin
   y:=ans[i];
   z:=nom[i];
   ans[i]:=ans[j];
   nom[i]:=nom[j];
   ans[j]:=y;
   nom[j]:=z;
   inc(i);
   dec(j);
  end;
 until(i>j);
 if j>l then Sort2(l,j);
 if r>i then Sort2(i,r);
end;
begin
readln(n,d);
for i:=1 to n do begin
 read(t[i]);
 nom[i]:=i;
end;
 Sort(1,n);
ch[1]:=1;
ans[1]:=1;
max:=1;
 
 for i:=2 to n do begin
  for j:=i-1 downto 1 do
   if t[i]-t[j]<=d
   then ch[ans[j]]:=0;
  for j:=1 to i do
   if ch[j]>0
   then break;
   if ch[j]=0
   then begin
    inc(max);
    ans[i]:=max;
   end
   else ans[i]:=ch[j];
  for j:=1 to max do
   ch[j]:=j;
  end;
 writeln(max);
 Sort2(1,n);
 for i:=1 to n do
  write(ans[i],' ');
end.