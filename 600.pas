var f1,f2: text;    flag,f:boolean;
i,j,a,c,l,k,s,n,p,b,min: integer;
r:string;
begin
assign(f1,'input.txt');
reset(f1);
assign(f2,'output.txt');
rewrite(f2);
 readln(f1,n);
 n:=n+1;
  for i:=2 to n do
    begin
     readln(f1,r);
     a:=0;
     c:=0;    flag:=false;
     b:=0;
     for j:=1  to length(r) do
       Begin
          if r[j]='0' then a:=a+1 else
          if r[j]='1' then b:=b+1 else
          if r[j]='2' then c:=c+1 ;
       end;
       f:=false;
     for j:=1 to length(r)-1 do
         begin
         Val(r[j],l,s);
         Val(r[j+1],k,s);
         if(l>k) then f:=true;
         end;
     if (a = b) and (b = c) and (c = a) and not(f)
     then flag:=true else flag:=false;
     if(flag) then writeln(f2,'YES')else writeln(f2,'NO');
    end;
close(f1);
Close(f2);
end.