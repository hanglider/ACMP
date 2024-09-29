program qq;
Type mass=array[1..9]of byte;
Var C:Set of byte;
    j,k,n,ResK:integer;
    Res:mass;
Function KRes:boolean;
var i:integer;
Begin
   KRes:=true;
   for i:=1 to n-1 do
      if abs(Res[i]-Res[i+1])>k
      then KRes:=false;
end;
Procedure Rec(j:integer);
Var i:integer;
Begin
   if j>N
   then Begin
           if KRes
           then inc(ResK);
   end
   else Begin
           for i:=1 to n do
           Begin
              if not(I in C)
              then Begin
                      Res[j]:=i;
                      C:=C+[i];
                      Rec(j+1);
                      C:=C-[i];
                   end;
           end;
        end;
End;
Begin
   ResK:=0;
   read(n);
   readln(k);
   j:=1;
   Rec(j);
   writeln(ResK);
end.