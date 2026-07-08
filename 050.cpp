#include <bits/stdc++.h>
using namespace std;
int main() {
    string a, b;
    cin >> a >> b;
    int n = a.size();
    int m = b.size();
    string bb = b + b;
    int c = 0;
    for (int i = 0; i + m <= n; i++) {
        string w = a.substr(i, m);
        if (bb.find(w) != string::npos)
            c++;
    }
    cout << c;
}
