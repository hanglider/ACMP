#include <bits/stdc++.h>
using namespace std;
short f[1 << 22];
int A[22], B[22], E[22], C[22], D[22];
int main() {
    freopen("INPUT.TXT", "r", stdin);
    int n;
    cin >> n;
    int t = 0;
    for (int i = 0; i < n; i++) {
        string s;
        int a, b, c, d;
        cin >> s >> a >> b >> c >> d;
        E[i] = s == "C";
        A[i] = a - c;
        B[i] = b - d;
        C[i] = c;
        D[i] = d;
        t += E[i];
    }
    int p = n - t;
    int X = 0;
    int M = 0;
    for (int i = 0; i < n; i++) {
        X += C[i] * (p - 1 + E[i]) + D[i] * (t - E[i]);
        M |= E[i] << i;
    }
    int F = 1 << n;
    f[F - 1] = 0;
    for (int S = F - 2; S >= 0; S--) {
        int h = __builtin_popcount(S & M);
        int u = __builtin_popcount(S) - h;
        int b = 1 << 30;
        for (int m = ~S & (F - 1); m; m &= m - 1) {
            int y = __builtin_ctz(m);
            int w = A[y] * u + B[y] * h + f[S | 1 << y];
            if (w < b) {
                b = w;
            }
        }
        f[S] = b;
    }
    cout << f[0] + X << " 0";
    int S = 0;
    for (int i = 0; i < n; i++) {
        int h = __builtin_popcount(S & M);
        int u = __builtin_popcount(S) - h;
        for (int y = 0; y < n; y++) {
            if (!(S >> y & 1) && A[y] * u + B[y] * h + f[S | 1 << y] == f[S]) {
                cout << " " << y + 1;
                S |= 1 << y;
                break;
            }
        }
    }
    cout << " 0\n";
}
