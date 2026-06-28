#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream in("input.txt");
    int n, k, c = 0;
    string s;
    in >> n >> k >> s;

    if (k >= n / 2) {
        cout << n * (n + 1) / 2;
        return 0;
    }

    for (int i = 0; i < 2 * n - 1; ++i) {
        for (int l = i / 2, r = (i + 1) / 2, m = 0; l >= 0 && r < n; --l, ++r) {
            if (s[l] != s[r] && ++m > k) break;
            ++c;
        }
    }
    cout << c;
    return 0;
}
