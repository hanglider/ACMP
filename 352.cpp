#include <bits/stdc++.h>

using namespace std;

long long gcd(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    long long n;
    if (cin >> n) {
        long long a = (n - 1) / 2;
        while (gcd(a, n) != 1) {
            a--;
        }
        cout << a << " " << n - a << "\n";
    }
    
    return 0;
}