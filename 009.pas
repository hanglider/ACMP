var a: array [1..10000] of integer;
    n: integer;
    t: text;
    max,i, min, sum, p, tmp: longint;
 
begin
     max:=1;
     min:=1;
     p:=1;
     sum:=0;
     readln(n);
     for i:=1 to n do
     begin
         read(a[i]);
         if (a[i]>a[max]) then max:=i;
         if (a[i]<a[min]) then min:=i;
         if (a[i]>0) then sum:=sum+a[i];
     end;
     if (min>max) then
     begin
          tmp:=min;
          min:=max;
          max:=tmp;
     end;
 
     for i:=(min+1) to max-1 do
         p:=p*a[i];
         write(sum,' ');
     write(p);
      
end.