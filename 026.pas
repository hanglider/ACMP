var x1,x2,y1,y2:integer;
    r,r1,r2:real;
    s:string;
begin
    read(f1,x1,y1,r1,x2,y2,r2);
    r:=sqrt(sqr(x1-x2)+sqr(y1-y2));
    if (r1+r2>=r) and (r+r2>=r1) and (r+r1>=r2) then s:='YES' else s:='NO';
    writeln(s);
end.