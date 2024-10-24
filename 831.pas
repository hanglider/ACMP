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
Function sum(x:integer):integer;
begin
  var c:integer;
  while x > 0 do
  begin
    c+=x mod 10;
    x:=x div 10
  end;
  Result:=c
end;
begin
  var mx:integer;
  var (a,b):=readinteger2;
  for var i:=a+1 to b do
    if prost(i) then 
      if sum(i)>sum(mx) then mx:=i 
                     else if sum(i)=sum(mx) then mx:=max(i,mx);
  if mx=0 then Print('-1') else mx.Print
end.