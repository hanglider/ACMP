#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    long long k;
    if (cin >> k) {
        if (k <= 2) {
            cout << 0 << "\n";
        } else if (k % 3 == 0) {
            cout << 2 << "\n";
        } else if (k % 4 == 0) {
            cout << 3 << "\n";
        } else {
            long long ans = -1;
            for (long long i = 5; i * i <= k; i += 2) {
                if (k % i == 0) {
                    ans = i - 1;
                    break;
                }
            }
            if (ans != -1) {
                cout << ans << "\n";
            } else if (k % 2 == 0) {
                cout << (k / 2) - 1 << "\n";
            } else {
                cout << k - 1 << "\n";
            }
        }
    }
    
    return 0;
}