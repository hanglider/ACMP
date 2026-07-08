#include <bits/stdc++.h>
using namespace std;
int a[100];
int d[100][100];
int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> a[i];
    for (int i = 0; i < n; i++)
        d[i][i] = a[i];
    for (int L = 2; L <= n; L++) {
        for (int i = 0; i + L - 1 < n; i++) {
            int j = i + L - 1;
            d[i][j] = max(a[i] - d[i+1][j], a[j] - d[i][j-1]);
        }
    }
    int r = d[0][n-1];
    if (r > 0)
        cout << 1;
    else if (r < 0)
        cout << 2;
    else
        cout << 0;
}
