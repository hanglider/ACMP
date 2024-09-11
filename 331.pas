var s,s1:string;
    a,b,ch,min,k:integer;
begin
  readln(s);
  readln(a,b);
  s1:=s[1];
  s1+=s[2];
  delete(s,1,3);
  val(s,min,k);
  val(s1,ch,k);
  ch+=a;
  min+=b;
  if min>=60 then begin
    ch+=min div 60;
    min:=min mod 60
  end;
  if ch>=24 then ch:=ch mod 24;
  if ch<10 then write('0',ch,':') else write(ch,':');
  if min<10 then write('0',min) else write(min)
end.