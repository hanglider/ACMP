var input,output:text;i,q,n,j,t,x,y:longint; ar:array[1..100,1..100] of longint;
begin
assign(input,'input.txt');reset(input);
assign(output,'output.txt');rewrite(output);
readln(input,n);
for i:=1 to n*2-1 do begin if i mod 2=1 then begin x:=0;y:=i+1; 
for t:=1 to i do begin inc(x);
dec(y);if (x>0) and (x<=n) and (y>0) and (y<=n) then begin inc(q);ar[x,y]:=q;end;end;end
else begin y:=0;x:=i+1;
for t:=1 to i do begin inc(y);dec(x);if (x>0) and (x<=n) and (y>0) and (y<=n) then begin inc(q);ar[x,y]:=q;end;end;end;end; 
for i:=1 to n do begin for j:=1 to n do begin write(output,ar[i,j],' ');end;writeln(output); end; 
close(output);close(input);
end.