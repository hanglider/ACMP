##
function time(a,b:integer):string;
begin
  var x,y:integer;
  var g:=min(a,b)-8*60;
  x:=g div 60;
  y:= g mod 60;
  var s:=x.ToString;
  var s1:=y.ToString;
  s+=' '+s1;
  result:=s
end;
var k:=readlninteger;
var t:=new Queue<integer>;
var ks1:=8*60;
var ks2:=ks1+5;
if k=1 then begin
  print('0 0');
  halt(0)
end else begin
while (ks1<20*60) and (ks2<20*60) and (k>1) do
begin
  if k>1 then begin
    ks1+=10;
    k-=1
  end;
  if k>1 then begin
    ks2+=10;
    k-=1
  end
end;
if k<>1 then print('NO') else
print(time(ks1,ks2))
end