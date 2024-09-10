##
Procedure zam(x,b:integer; a:array of integer; f:array of boolean);
begin
  for var i:=0 to a.high do
    if (a[i]=x) and (f[i]=false) then begin
       a[i]:=b;
       f[i]:=true
    end
end;
var n:=readlninteger;
var a:=readarrinteger(n);
var f:=new boolean[n];
var m:=readlninteger;
for var i:=1 to m do
begin
  zam(readinteger,readlninteger,a,f);  
end;
a.Print