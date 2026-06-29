#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream in("input.txt");
    string s;
    getline(in, s);
    int m = 1;
    for (char c : s) {
        if (c == '\r') continue;
        if (c >= '0' && c <= '9') m = max(m, c - '0');
        else if (c >= 'A' && c <= 'Z') m = max(m, c - 'A' + 10);
        else return cout << -1, 0;
    }
    cout << m + 1 << '\n';
}
