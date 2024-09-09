var c: char;
    f: text;
 
begin
     assign(f,'input.txt');
     reset(f);
     readln(f,c);
     close(f);
     assign(f,'output.txt');
     rewrite(f);
     case c of
          'q': writeln(f,'w');
          'w': writeln(f,'e');
          'e': writeln(f,'r');
          'r': writeln(f,'t');
          't': writeln(f,'y');
          'y': writeln(f,'u');
          'u': writeln(f,'i');
          'i': writeln(f,'o');
          'o': writeln(f,'p');
          'p': writeln(f,'a');
          'a': writeln(f,'s');
          's': writeln(f,'d');
          'd': writeln(f,'f');
          'f': writeln(f,'g');
          'g': writeln(f,'h');
          'h': writeln(f,'j');
          'j': writeln(f,'k');
          'k': writeln(f,'l');
          'l': writeln(f,'z');
          'z': writeln(f,'x');
          'x': writeln(f,'c');
          'c': writeln(f,'v');
          'v': writeln(f,'b');
          'b': writeln(f,'n');
          'n': writeln(f,'m');
          'm': writeln(f,'q');
     end;
     close(f);
end.