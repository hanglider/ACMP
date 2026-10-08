#include <bits/stdc++.h>
using namespace std;

int sz;
vector<int> tree;  // segment tree of counts, minimum on ranges

void increment(int pos) {
    pos += sz;
    tree[pos]++;
    for (pos /= 2; pos >= 1; pos /= 2) tree[pos] = min(tree[2 * pos], tree[2 * pos + 1]);
}

int prefixMin(int r) {  // min over [0, r)
    int res = INT_MAX;
    for (int l = sz, rr = r + sz; l < rr; l /= 2, rr /= 2) {
        if (l & 1) res = min(res, tree[l++]);
        if (rr & 1) res = min(res, tree[--rr]);
    }
    return res;
}

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    sz = 1;
    while (sz < n + 1) sz *= 2;
    tree.assign(2 * sz, 0);
    vector<int> cnt(n + 1, 0);
    int answer = 0;
    for (int j = 0; j < n; j++) {
        int x;
        scanf("%d", &x);
        cnt[x]++;
        increment(x);
        if (x > 0 && prefixMin(x) < cnt[x] - k) break;
        answer = j + 1;
    }
    printf("%d\n", answer);
}
