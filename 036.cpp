#include "bits/stdc++.h"

#pragma GCC target("avx2")
#pragma GCC optimization("O3")
#pragma GCC optimization("unroll-loops")

bool is_prime(int x) {
    if (x < 2) return false;
    if (x == 2)return true;
    if (!(x & 1)) return false;
    for (int j = 3; j * j <= x; ++j)
        if (!(x % j)) return false;
    return true;
}

using namespace std;
int main() {
    int n;
    cin >> n;
    int ans = 0;
    for (int i = n + 1; i < 2*n; i++) {
        if (is_prime(i)) {ans++;}
    }
    cout << ans;
    //system("pause");
}