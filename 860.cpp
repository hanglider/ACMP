#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct VecHash {
    size_t operator()(const vector<int>& v) const noexcept {
        size_t h = 0;
        for (int x : v) h = h * 239017 + (x + 1);
        return h;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector<string> a(N);
    for (int i = 0; i < N; i++) cin >> a[i];

    if (N < M) {
        vector<string> b(M, string(N, '#'));
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                b[j][i] = a[i][j];
        swap(N, M);
        a = b;
    }

    vector<unordered_map<vector<int>, ll, VecHash>> dp(N + 1);
    dp[0][vector<int>(M, 0)] = 1;

    for (int r = 0; r < N; r++) {
        for (auto &[state, ways] : dp[r]) {
            vector<int> cur = state;
            for (int i = 0; i < M; i++)
                if (cur[i] > 0) cur[i]--;

            function<void(int, vector<int>&)> dfs = [&](int c, vector<int>& h) {
                while (c < M && (a[r][c] == '#' || h[c] > 0)) c++;
                if (c >= M) { dp[r + 1][h] += ways; return; }

                int maxk = min({M - c, N - r});
                for (int k = 1; k <= maxk; k++) {
                    bool ok = true;
                    for (int x = 0; x < k && ok; x++) {
                        if (h[c + x] != 0) ok = false;
                        for (int y = 0; y < k && ok; y++)
                            if (a[r + y][c + x] == '#') ok = false;
                    }
                    if (!ok) break;
                    vector<int> nh = h;
                    for (int x = 0; x < k; x++) nh[c + x] = k - 1;
                    dfs(c + k, nh);
                }
            };
            dfs(0, cur);
        }
    }

    ll ans = 0;
    for (auto &[st, v] : dp[N]) {
        bool ok = true;
        for (int x : st)
            if (x != 0) { ok = false; break; }
        if (ok) ans += v;
    }
    cout << ans << "\n";
}
