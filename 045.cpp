#include <bits/stdc++.h>
using namespace std;
int main() {
    long long n;
    cin >> n;
    if (n == 0) {
        cout << 10;
        return 0;
    }
    vector<int> d;
    for (int p = 9; p >= 2; p--) {
        while (n % p == 0) {
            d.push_back(p);
            n /= p;
        }
    }
    if (n > 1) {
        cout << -1;
        return 0;
    }
    if (d.empty()) {
        cout << 1;
        return 0;
    }
    sort(d.begin(), d.end());
    for (int x : d)
        cout << x;
}
