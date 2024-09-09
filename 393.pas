var nv,v:array [1..1000] of string;
    d,nm,a,vm:array [1..1000] of longint;
    s:string;
    su,st,sc,n,i,j,k,m:longint;
    c:integer;
begin
 readln(n);
  for i:=1 to n do begin
   readln(s);
   nv[i]:=copy(s,1,pos(' ',s)-1);
   delete(s,1,pos(' ',s));
   val(s,vm[i],c);
  end;
  readln(m,k);
  for i:=1 to m do
   readln(v[i]);
  for i:=1 to k do
   read(d[i]);
i:=1;
  while (sc<m) do begin
   for j:=1 to m do
    if v[j]=nv[i]
    then begin
     nm[j]:=i;
     inc(sc);
    end;
   inc(i);
  end;
st:=1;
 for i:=1 to m do begin
  inc(su,vm[nm[i]]);
  if (su>d[st]) and (st<=k)
  then begin
   dec(a[nm[i]]);
   su:=d[st];
   inc(st);
  end
  else inc(a[nm[i]]);
 end;

 for i:=1 to n do
  write(a[i],' ');
end.