#include "bits/stdc++.h"
 
using ll = long long;
 
using namespace std;
 
int Binpow (ll a, ll n) {int r = 1;while (n) {if (n & 1) r *= a; a *= a; n >>= 1;} return r;}
 
ll n,nn,kol,ans;
int main() {
    cin >> nn;
    n = nn;
    ans = 1;
    while (n % 2 == 0) {
        n >>= 1;
        kol++;
    }
    ans = ll(Binpow(2, kol));
    kol = -1;
    n >>= 1;
    while (n % 2 != 0) {
        n >>= 1;
        kol++;
        ans += Binpow(2, kol);
    }
    cout << nn + ans;
    return 0;
}