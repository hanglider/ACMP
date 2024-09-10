##
var a:=new int64[50];
a[0]:=1;
a[1]:=1;
for var i:=2 to a.High do
begin
  a[i]:=a[i-1]+a[i-2]
end;
var x:=readlnint64;
if a.IndexOf(x)=-1 then Print('0') 
else begin
  Println('1');
  Println(a.IndexOf(x)+1)
end