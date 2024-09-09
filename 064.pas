var
  primes := new List<longword>;
 
function is_prime(x: longword): boolean;
begin
  primes.add(x);
  var i := 0;
  while x mod primes[i] <> 0 do
    inc(i);
  primes.removelast;
  result := i = primes.count;
end;
 
function to_list(x: longword): List<byte>;
begin
  result := new List<byte>;
  while x <> 0 do
  begin
    result.add(x mod 10);
    x := x div 10;
  end;
  result.reverse;
end;
 
begin
  primes.add(2);
  var m := ReadInteger;
  var tests := new List<longword>;
  var max_pos := 0;
  loop m do
  begin
    var a := ReadInteger;
    tests.add(a);
    if a > max_pos then
      max_pos := a;
  end;
  var str := new List<byte>;
  str.add(2);
  var i := 3;
  while str.count <= max_pos do
  begin
    if is_prime(i) then
    begin
      primes.add(i);
      str += to_list(i);
    end;
    inc(i, 2);  
  end;
  foreach var test in tests do
    write(str[test-1]);
end.