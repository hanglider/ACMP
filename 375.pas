Var
  m, k: integer;
  s,d,d1: string;
  p:biginteger;
procedure perevod(m: biginteger; k:integer; s: string);
var
  z:biginteger;
  x,err:integer;
  str:String;
const
  digit:string[36]='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
begin
  if s[1]='0' then begin
    Print('0');
    halt(0)
  end;
     
  for var i:=1 to length(s) do
    z:=z*m+pos(s[i],digit)-1;
repeat  
    p:=z mod k;
    d:=p.ToString;
    val(d,x,err); 
    str:=digit[x+1]+str;
    z:=z div k;
  until z=0;
  Print(str)
end;
begin
  readln(m,k);
  readln(s);
  str(k,d);
  str(m,d1);
  var a:=d1.ToBigInteger;
  var b:=d.ToBigInteger;
  perevod(a, k ,s );
end.