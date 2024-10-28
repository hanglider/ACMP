type mass = array [1..200000] of int64;
     mas = array [1..200000] of string[3];
var a,b,nom:mass;
    ss:mas;
    i,j,n,k,st:longint;
Procedure Sort2(l,r:longint);
var i,j,x,y,z:int64;
begin
 i:=l;
 j:=r;
 x:=b[(i+j) div 2];
 repeat
  while (b[i]<x) do inc(i);
  while (b[j]>x) do dec(j);
  if i<=j
  then begin
   y:=b[i];
   z:=nom[i];
   b[i]:=b[j];
   nom[i]:=nom[j];
   b[j]:=y;
   nom[j]:=z;
   inc(i);
   dec(j);
  end;
 until (i>j);
 if l<j then Sort2(l,j);
 if i<r then Sort2(i,r);
end;

Procedure Sort3(l,r:longint);
var i,j,x,y:longint;
    z:string;
begin
 i:=l;
 j:=r;
 x:=nom[(i+j) div 2];
 repeat
  while (nom[i]<x) do inc(i);
  while (nom[j]>x) do dec(j);
  if i<=j
  then begin
   y:=nom[i];
   z:=ss[i];
   nom[i]:=nom[j];
   ss[i]:=ss[j];
   nom[j]:=y;
   ss[j]:=z;
   inc(i);
   dec(j);
  end;
 until (i>j);
 if l<j then Sort3(l,j);
 if i<r then Sort3(i,r);
end;

begin
 readln(n,k);
 for i:=1 to n do
  read(a[i]);
 for i:=1 to k do begin
  read(b[i]);
  nom[i]:=i;
 end;

 Sort2(1,k);
st:=1;
 for i:=1 to k do begin
   while ((b[i]>a[st]) and (st<n)) do inc(st);
    if b[i]=a[st]
    then ss[i]:='YES'
    else ss[i]:='NO';
 end;
 Sort3(1,k);
 for i:=1 to k do
  write(ss[i],' ');
end.