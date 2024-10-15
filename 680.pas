var
  n, i: integer;
  ans: int64;

begin
  readln(n);
  {if n = 0
    then ans := 0
  else} begin
    ans := 3;
    for i := 2 to n do
    begin
      ans := ans * 2;
    end;
  end;
  writeln(ans);
  readln;
end.