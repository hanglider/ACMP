#include <bits/stdc++.h>

using namespace std;

int bit_tree[10005];
int n;

void add(int idx, int val) {
    for (; idx <= n; idx += idx & -idx) {
        bit_tree[idx] += val;
    }
}

int query(int idx) {
    int sum = 0;
    for (; idx > 0; idx -= idx & -idx) {
        sum += bit_tree[idx];
    }
    return sum;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int k;
    if (cin >> n >> k) {
        long long total_pushups = 0;
        for (int r = 0; r < k; ++r) {
            memset(bit_tree, 0, sizeof(bit_tree));
            for (int i = 0; i < n; ++i) {
                int height;
                cin >> height;
                total_pushups += i - query(height);
                add(height, 1);
            }
        }
        cout << total_pushups << "\n";
    }

    return 0;
}