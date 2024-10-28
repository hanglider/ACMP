##
Function prost(x:integer):boolean;
label m1;
begin
  for var i:=2 to x.Sqrt.Trunc do
    if x mod i=0 then begin
      Result:=false;
      goto m1
    end;
  Result:=true;
  m1:
end;
var a:=new integer[1000];
a[0]:=2;
a[1]:=3;
var t:integer:=2;
for var i:=5 to 1024 do
  if prost(i) then begin
     a[t]:=i;
     t+=1
  end;
setlength(a,t);
var n:=readlninteger;
var c:=readarrinteger(n);
var b:=new integer[n];
for var i:=0 to c.High do
  for var j:=0 to a.High do
    if c[i] mod a[j]= 0 then b[i]+=1;
//b.Print;
var f:=b.Max;
var lst:=new List <integer>;
for var i:=0 to c.High do
  if b[i]=f then lst.Add(c[i]);
lst.Sort;
print(lst[0])