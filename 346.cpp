#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ifstream in("input.txt");
    string a, b;
    long long c;
    in >> a >> b >> c;
    
    int tb[10] = {};
    for (char ch : b) tb[ch - '0']++;
    sort(a.begin(), a.end());
    
    do {
        long long x = 0;
        for (char ch : a) x = x * 10 + (ch - '0');
        long long y = c - x, t = y;
        
        if (y >= 0) {
            int cb[10] = {};
            for (int i = 0; i < b.size(); ++i) {
                cb[t % 10]++;
                t /= 10;
            }
            if (t == 0) {
                bool ok = true;
                for (int j = 0; j < 10; ++j) ok &= (cb[j] == tb[j]);
                if (ok) return cout << "YES\n" << x << " " << y << '\n', 0;
            }
        }
    } while (next_permutation(a.begin(), a.end()));
    
    cout << "NO\n";
}
