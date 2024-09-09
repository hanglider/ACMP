type bc = set of integer;
var a,b,x,i,j:integer;
    c,k:bc;
begin
  readln(a,b);
  c:=[];
  x:=10;
  var g:=a;
  for var ii:=1 to 4 do
  begin
    c+=[a mod x];
    a:=a div x;
  end;
  var bic,cow:integer;
  for var ii:=1 to 4 do
  begin
    i:=g mod x; j:= b mod x;
    if i=j then inc(bic);
    if j in c then inc(cow);
    g:=g div x; b:=b div x
  end;
  Print(bic, cow-bic)
end.