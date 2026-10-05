#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<long long> g(n);
    for (auto &x : g) cin >> x;
    vector<int> order(n);
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [&](int a, int b) { return g[a] > g[b]; });
    vector<long long> pre(n + 1, 0);
    for (int i = 0; i < n; i++) pre[i + 1] = pre[i] + g[order[i]];

    const long long INF = LLONG_MAX / 4;
    // f[i][j]: first i kids (sorted by greed desc) got j cookies in total, counts nonincreasing
    vector<vector<long long>> f(n + 1, vector<long long>(m + 1, INF));
    vector<vector<int>> from(n + 1, vector<int>(m + 1, -1));  // -1: shift all by one; k: kids k+1..i got 1
    f[0][0] = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = i; j <= m; j++) {
            if (f[i][j - i] < f[i][j]) {
                f[i][j] = f[i][j - i];
                from[i][j] = -1;
            }
            for (int k = 0; k < i; k++) {
                long long prev = f[k][j - (i - k)];
                if (prev >= INF) continue;
                long long cost = prev + (long long)k * (pre[i] - pre[k]);
                if (cost < f[i][j]) {
                    f[i][j] = cost;
                    from[i][j] = k;
                }
            }
        }
    }

    vector<long long> cnt(n, 0);
    int i = n, j = m;
    long long add = 0;
    while (i > 0) {
        int k = from[i][j];
        if (k == -1) {
            add++;
            j -= i;
        } else {
            for (int t = k; t < i; t++) cnt[order[t]] = 1 + add;
            j -= i - k;
            i = k;
        }
    }
    cout << f[n][m] << "\n";
    for (int t = 0; t < n; t++) cout << cnt[t] << (t + 1 < n ? " " : "\n");
}
