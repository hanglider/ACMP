#include <iostream>
#include <map>
using namespace std;
 
#define ll long long
ll n, x = 2, m, y, mn = 2e9;
map <ll, ll> a, b;
int main() {
    cin >> n;
    m = n;
    while (n > 1 && x * x <= n) {
        if (n % x == 0) {
            a[x]++;
            n /= x;
        }
        else x++;
    }
    a[n]++;
    if (a.size() == 0)
        cout << 1;
    else {
        for (auto c : a) {
            y = x = c.first;
            n = m;
            while (x <= m) {
                b[c.first] += m / x;
                x *= y;
            }
        }
 
        for (auto c : b)
            if (b[c.first] / a[c.first] < mn)
                mn = b[c.first] / a[c.first];
 
        cout << mn;
    }
}