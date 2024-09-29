п»їvar k,n: longint;
begin
     readln(n);
     k:=n- n div 2 - n div 3 - n div 5 - n div 30;
     k:=k+(n div 10)+(n div 6)+(n div 15);
     writeln(k);

end.