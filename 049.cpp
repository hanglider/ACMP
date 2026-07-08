#include <bits/stdc++.h>
using namespace std;
void R(char c, int &l, int &r) {
    if (c >= '0' && c <= '9') {
        l = r = c - '0';
    } else if (c == '?') {
        l = 0;
        r = 9;
    } else {
        l = c - 'a';
        r = l + 3;
    }
}
int main() {
    string p, q;
    cin >> p >> q;
    long long t = 1;
    for (int i = 0; i < (int)p.size(); i++) {
        int l1, r1, l2, r2;
        R(p[i], l1, r1);
        R(q[i], l2, r2);
        int l = max(l1, l2);
        int r = min(r1, r2);
        t *= max(0, r - l + 1);
    }
    cout << t;
}
