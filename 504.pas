var
   c1,c2,c3,c: char;
   i, n: integer;
   f: text;

begin
     c1:='G';
     c2:='C';
     c3:='V';
     readln( n);
    
     for i:=1  to n do
     begin
          c:=c2;
          c2:=c3;
          c3:=c;

          c:=c2;
          c2:=c1;
          c1:=c;
     end;
     writeln(c1,c2,c3);
     
end.
