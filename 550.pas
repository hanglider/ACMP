var n:longint;
    s:string;
begin
    
    assign(input,'INPUT.TXT');
    reset(input);
    assign(output,'OUTPUT.TXT');
    rewrite(output);
 
    read(n);
    str(n,s);
    while length(s)<4 do s:='0'+s;
    if ((n mod 4=0)and(n mod 100<>0))or(n mod 400=0) then write('12/09/',s) else write('13/09/',s);
 
end. 