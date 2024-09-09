#include "bits/stdc++.h"

using namespace std;
int main() {
    int n;
    string s;
    cin >> n >> s;
    long long ans = 1;
    for (int i = n; i > 0; i -= s.size()) {
        ans *= i;
    }
    cout << ans;
    //system("pause");
}