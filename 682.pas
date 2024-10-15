begin
  var n := ReadInteger;
  var k := Biginteger(10) ** (n - 1);
  Print(9 * k * (11 * k - 1) div 2)
end.