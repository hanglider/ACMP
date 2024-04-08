var
   a,b,r: array[1..1000] of byte;
   la,lb,lc,i,mem,tm: integer;
   c: char;
   f: text;
 
begin
     assign(f,'input.txt');
     reset(f);
     i:=0;
     repeat
           read(f,c);
           if (c in ['0'..'9']) then
           begin
                la:=la+1;
                a[la]:=ord(c)-48;
           end;
     until not(c in ['0'..'9']);
 
     repeat read(f,c); until (c in ['0'..'9'])or(eof(f));
 
     lb:=1;
     b[lb]:=ord(c)-48;
 
     repeat
           read(f,c);
           if (c in ['0'..'9']) then
           begin
                lb:=lb+1;
                b[lb]:=ord(c)-48;
           end;
     until not(c in ['0'..'9'])or(eof(f));
     close(f);
 
     la:=la+1;
     lb:=lb+1;
     for i:=1 to la div 2 do begin
         mem:=a[i];
         a[i]:=a[la-i];
         a[la-i]:=mem;
     end;
 
     for i:=1 to lb div 2 do begin
         mem:=b[i];
         b[i]:=b[lb-i];
         b[lb-i]:=mem;
     end;
     la:=la-1;
     lb:=lb-1;
     mem:=0;
 
     if la>lb then tm:=la else tm:=lb;
     for i:=1 to tm do
     begin
          r[i]:=a[i]+b[i]+mem;
          mem:=0;
          if r[i]>9 then begin
             r[i]:=r[i]-10;
             mem:=1;
          end;
     end;
 
 
 
     if mem=1 then begin
        tm:=tm+1;
        r[tm]:=1;
     end;
 
     tm:=tm+1;
     for i:=1 to tm div 2 do begin
         mem:=r[i];
         r[i]:=r[tm-i];
         r[tm-i]:=mem;
     end;
     tm:=tm-1;
 
     assign(f,'output.txt');
     rewrite(f);
     for i:=1 to tm do write(f,r[i]);
     close(f);
end.