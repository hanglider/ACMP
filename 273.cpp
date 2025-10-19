#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;
    int n = s.size();

    set<string> uniq;

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            for (int k = j + 1; k < n; ++k) {
                if (s[i] == '0') continue; 
                string num;
                num.push_back(s[i]);
                num.push_back(s[j]);
                num.push_back(s[k]);
                uniq.insert(num);
            }
        }
    }

    cout << uniq.size() << "\n";
    return 0;
}
