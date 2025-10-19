#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N; long long C; int K;
    if (!(cin >> N >> C >> K)) return 0;
    string s;
    cin >> s;

    unsigned long long MOD = 1;
    for (int i = 0; i < K; ++i) MOD *= 10ull;

    vector<unsigned long long> dp(N + 1, 0);
    dp[0] = 1;

    int maxLen = to_string(C).size();

    for (int i = 0; i < N; ++i) {
        if (dp[i] == 0) continue;

        if (s[i] == '0') {
            if (0 <= C) {
                dp[i + 1] += dp[i];
                if (dp[i + 1] >= MOD) dp[i + 1] -= MOD;
            }
            continue;
        }

        long long val = 0;
        for (int j = i; j < N && j - i + 1 <= maxLen; ++j) {
            val = val * 10 + (s[j] - '0');
            if (val > C) break;

            dp[j + 1] += dp[i];
            if (dp[j + 1] >= MOD) dp[j + 1] -= MOD;
        }
    }

    unsigned long long ans = dp[N] % MOD;

    string out = to_string(ans);
    int pos = 0;
    while (pos + 1 < (int)out.size() && out[pos] == '0') ++pos;
    cout << out.substr(pos) << '\n';

    return 0;
}
