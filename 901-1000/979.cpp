#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<long long> x(n), y(n);
    unordered_map<long long, int> id;
    id.reserve(4 * n);
    const long long OFF = 1000000001LL, M = 2000000003LL;
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld", &x[i], &y[i]);
        id[(x[i] + OFF) * M + (y[i] + OFF)] = i;
    }
    // state = prev * n + cur; velocity = pos[cur] - pos[prev]
    vector<int> par(n * n, -2);
    queue<int> q;
    int start = 0 * n + 0;
    par[start] = -1;
    q.push(start);
    int found = -1;
    while (!q.empty()) {
        int s = q.front();
        q.pop();
        int a = s / n, b = s % n;
        if (b == n - 1) {
            found = s;
            break;
        }
        long long dx = x[b] - x[a], dy = y[b] - y[a];
        for (int ex = -1; ex <= 1; ex++)
            for (int ey = -1; ey <= 1; ey++) {
                long long nx = x[b] + dx + ex, ny = y[b] + dy + ey;
                if (nx < -1000000000LL || nx > 1000000000LL || ny < -1000000000LL || ny > 1000000000LL)
                    continue;
                auto it = id.find((nx + OFF) * M + (ny + OFF));
                if (it == id.end()) continue;
                int t = b * n + it->second;
                if (par[t] != -2) continue;
                par[t] = s;
                q.push(t);
            }
    }
    if (found < 0) {
        printf("-1\n");
        return 0;
    }
    vector<int> path;
    for (int s = found; s != -1; s = par[s]) path.push_back(s % n);
    reverse(path.begin(), path.end());
    printf("%d\n", (int)path.size() - 1);
    for (size_t i = 0; i < path.size(); i++) printf("%d%c", path[i] + 1, i + 1 == path.size() ? '\n' : ' ');
}
