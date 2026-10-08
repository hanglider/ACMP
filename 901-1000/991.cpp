#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<vector<char>> has(n, vector<char>(k, 0));
    vector<int> owned(n, 0);
    vector<int> holders(k, 1);
    vector<vector<int>> received(n, vector<int>(n, 0));  // received[x][y]: fragments x got from y
    vector<int> doneAt(n, 0);
    for (int f = 0; f < k; f++) has[0][f] = 1;
    owned[0] = k;
    int incomplete = n - 1;

    int round = 0;
    while (incomplete > 0) {
        round++;
        vector<int> wantFrag(n, -1), wantFrom(n, -1);
        for (int c = 0; c < n; c++) {
            if (owned[c] == k) continue;
            int best = -1;
            for (int f = 0; f < k; f++)
                if (!has[c][f] && (best == -1 || holders[f] < holders[best])) best = f;
            int src = -1;
            for (int s = 0; s < n; s++)
                if (s != c && has[s][best] && (src == -1 || owned[s] < owned[src])) src = s;
            wantFrag[c] = best;
            wantFrom[c] = src;
        }
        vector<int> chosen(n, -1);
        for (int c = 0; c < n; c++) {
            if (wantFrom[c] < 0) continue;
            int x = wantFrom[c];
            int cur = chosen[x];
            if (cur == -1) {
                chosen[x] = c;
                continue;
            }
            if (received[x][c] != received[x][cur]) {
                if (received[x][c] > received[x][cur]) chosen[x] = c;
            } else if (owned[c] < owned[cur]) {
                chosen[x] = c;
            }
        }
        for (int x = 0; x < n; x++) {
            int c = chosen[x];
            if (c < 0) continue;
            int f = wantFrag[c];
            has[c][f] = 1;
            owned[c]++;
            holders[f]++;
            received[c][x]++;
            if (owned[c] == k) {
                doneAt[c] = round;
                incomplete--;
            }
        }
    }
    for (int c = 1; c < n; c++) cout << doneAt[c] << (c + 1 < n ? " " : "\n");
}
