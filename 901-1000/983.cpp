#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    vector<int> t(n), w(n), order(n);
    for (int i = 0; i < n; i++) {
        if (scanf("%d %d", &t[i], &w[i]) != 2) return 0;
        order[i] = i;
    }
    sort(order.begin(), order.end(), [&](int a, int b) { return w[a] < w[b]; });
    vector<long long> answer(n);
    long long finish = 0;
    for (int i : order) {
        finish = max(finish, (long long)t[i] * w[i]);
        answer[i] = finish;
    }
    for (int i = 0; i < n; i++) printf("%lld\n", answer[i]);
}
