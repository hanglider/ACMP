const n=100000;
Label m2;
var a:array of integer;
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
begin
  a:=new integer[n];
  var k:=readinteger;
  a[0]:=2;
  a[1]:=3;
  var d:=2;
  for var i:=5 to n do
    if prost(i) then begin
       a[d]:=i;
       inc(d)
    end;
  var p:=0;
  var j:=0;
  for var i:=1 to n do
  begin
    if prost(i+1) then inc(p);
    j:=i;
    if p=k then goto m2
  end;
  m2:
  a[j].Println; 
end.