#include <iostream>
#include <string>
using namespace std;
int n, i, r, x, y, z, m=30001,c;
string s, ch, t, b;

int a(int i) {
    ch = "";
    n = 1;
    if (s[i] == '-') {
        n = -1;
        i++;
    }
    while (s[i] >= '0' && s[i] <= '9') {
        ch += s[i];
        i++;
    }
    r = i;
    if (ch != "")
        return stoi(ch) * n;
    else return m;
}
int main() {
    getline(cin, s);
    if (s.find(" ") != string::npos) {
        cout << "ERROR";
        return 0;
    }

    x = a(0);
    if ((x == m) || (s[r] != '+' && s[r] != '-' && s[r] != '*' && s[r] != '/'))
        c=1;
    else {
        t = s[r];
        y = a(r + 1);
        if ((y == m) || (s[r] != '='))
            c = 1;
        else {
            b = s[r];
            z = a(r + 1);
            if (z == m || r < s.size())
                c = 1;
            else {
                double l = x;
                if (t == "+")
                    l = x + y;
                if (t == "-")
                    l = x - y;
                if (t == "*")
                    l = x * y;
                if (t == "/")
                    l = double(x) / y;
                if (l == z)
                    cout << "YES";
                else cout << "NO";
            }
        }
    }
    if (c == 1)
        cout << "ERROR";
    return 0;
}