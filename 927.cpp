#include <bits/stdc++.h>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    string S;
    if (!(cin >> S)) return 0;

    int n = S.length();
    long long dp[2][10][10] = {0};
    
    int start_d = (n == 1) ? 1 : 0;
    int c = S[n-1] - '0';
    
    for(int da = start_d; da <= 9; ++da) {
        for(int db = start_d; db <= 9; ++db) {
            int sum = da + db;
            if (sum % 10 == c) {
                dp[sum / 10][da][db] = 1;
            }
        }
    }

    for(int i = n - 2; i >= 0; --i) {
        c = S[i] - '0';
        long long next_dp[2][10][10] = {0};
        start_d = (i == 0) ? 1 : 0;

        for(int carry_in = 0; carry_in <= 1; ++carry_in) {
            long long total = 0;
            long long sum_a[10] = {0};
            long long sum_b[10] = {0};

            for(int pa = 0; pa <= 9; ++pa) {
                for(int pb = 0; pb <= 9; ++pb) {
                    long long val = dp[carry_in][pa][pb];
                    if (val > 0) {
                        total = (total + val) % MOD;
                        sum_a[pa] = (sum_a[pa] + val) % MOD;
                        sum_b[pb] = (sum_b[pb] + val) % MOD;
                    }
                }
            }

            if (total == 0) continue; 

            for(int da = start_d; da <= 9; ++da) {
                for(int db = start_d; db <= 9; ++db) {
                    int sum = da + db + carry_in;
                    if (sum % 10 == c) {
                        long long ways = total - sum_a[da] - sum_b[db] + dp[carry_in][da][db];
                        ways %= MOD;
                        if (ways < 0) ways += MOD;

                        int carry_out = sum / 10;
                        next_dp[carry_out][da][db] = (next_dp[carry_out][da][db] + ways) % MOD;
                    }
                }
            }
        }
        
        for(int carry = 0; carry <= 1; ++carry) {
            for(int da = 0; da <= 9; ++da) {
                for(int db = 0; db <= 9; ++db) {
                    dp[carry][da][db] = next_dp[carry][da][db];
                }
            }
        }
    }

    long long ans = 0;
    for(int da = 0; da <= 9; ++da) {
        for(int db = 0; db <= 9; ++db) {
            ans = (ans + dp[0][da][db]) % MOD;
        }
    }

    cout << ans << "\n";

    return 0;
}