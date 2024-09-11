program qq;
Var s,s1:string;
    used:array[0..10]of boolean;
    a:array[0..10]of longint;
    i,n,j:longint;
    ch:char;
procedure dfs(v:longint);
var i:longint;
begin
 if (v=n+1)
  then
   begin
    for i:= 1 to n do
     write(s[a[i]]);
     writeln;
    exit;
   end;
  for i:= 1 to n do
   if used[i] then
    begin
     a[v]:=i;
     used[i]:=false;
     dfs(v+1);
     used[i]:=true;
    end;
end;
Begin
   readln(s);
   n:=length(s);
   for i:=1 to n-1 do
      for j:=1 to n-i do
         if (s[j]>s[j+1])
         then begin
                 ch:=s[j];
                 s[j]:=s[j+1];
                 s[j+1]:=ch;
              end;
   for i:=1 to n do
      used[i]:=true;
   dfs(1);
end.