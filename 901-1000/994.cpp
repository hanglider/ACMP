#include <bits/stdc++.h>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;
    int n = a.size(), m = b.size();

    // pre[i][j]: longest common substring of a[0..i) and b[0..j)
    vector<vector<short>> pre(n + 1, vector<short>(m + 1, 0));
    vector<short> endPrev(m + 1, 0), endCur(m + 1, 0);
    for (int i = 1; i <= n; i++) {
        endCur[0] = 0;
        for (int j = 1; j <= m; j++) {
            endCur[j] = (a[i - 1] == b[j - 1]) ? endPrev[j - 1] + 1 : 0;
            pre[i][j] = max({pre[i - 1][j], pre[i][j - 1], endCur[j]});
        }
        swap(endPrev, endCur);
    }

    // suf[i][j]: longest common substring of a[i..) and b[j..), rolled over i
    vector<short> sufNext(m + 2, 0), sufCur(m + 2, 0);
    vector<short> startNext(m + 2, 0), startCur(m + 2, 0);
    int best = -1, bi = 0, bj = 0;
    for (int i = n; i >= 0; i--) {
        sufCur[m] = 0;
        startCur[m] = 0;
        for (int j = m; j >= 0; j--) {
            if (i < n && j < m) {
                startCur[j] = (a[i] == b[j]) ? startNext[j + 1] + 1 : 0;
                sufCur[j] = max({sufNext[j], sufCur[j + 1], startCur[j]});
            } else {
                startCur[j] = 0;
                sufCur[j] = 0;
            }
            int total = pre[i][j] + sufCur[j];
            if (total > best) {
                best = total;
                bi = i;
                bj = j;
            }
        }
        swap(sufNext, sufCur);
        swap(startNext, startCur);
    }

    // recover the two strings for the best split
    int lenA = pre[bi][bj], lenB = best - lenA;
    string alpha, beta;
    if (lenA > 0) {
        vector<int> prev(bj + 1, 0), cur(bj + 1, 0);
        bool found = false;
        for (int i = 1; i <= bi && !found; i++) {
            for (int j = 1; j <= bj; j++) {
                cur[j] = (a[i - 1] == b[j - 1]) ? prev[j - 1] + 1 : 0;
                if (cur[j] == lenA) {
                    alpha = a.substr(i - lenA, lenA);
                    found = true;
                    break;
                }
            }
            swap(prev, cur);
        }
    }
    if (lenB > 0) {
        vector<int> next(m + 2, 0), cur(m + 2, 0);
        bool found = false;
        for (int i = n - 1; i >= bi && !found; i--) {
            for (int j = m - 1; j >= bj; j--) {
                cur[j] = (a[i] == b[j]) ? next[j + 1] + 1 : 0;
                if (cur[j] == lenB) {
                    beta = a.substr(i, lenB);
                    found = true;
                    break;
                }
            }
            swap(next, cur);
        }
    }
    cout << alpha << "\n" << beta << "\n";
}
