#include <cstdio>
#include <utility>
#include <vector>
using namespace std;

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2) return 0;
    vector<vector<int>> tree(n + 1);
    vector<pair<int, int>> dirt;
    for (int i = 0; i < m; i++) {
        int a, b, stone;
        if (scanf("%d %d %d", &a, &b, &stone) != 3) break;
        if (stone == 1) {
            tree[a].push_back(b);
            tree[b].push_back(a);
        } else {
            dirt.push_back({a, b});
        }
    }

    // root the stone tree at the capital
    vector<int> depth(n + 1, -1), parent(n + 1, 0), order;
    order.reserve(n);
    order.push_back(1);
    depth[1] = 0;
    for (size_t i = 0; i < order.size(); i++) {
        int v = order[i];
        for (int w : tree[v]) {
            if (depth[w] < 0) {
                depth[w] = depth[v] + 1;
                parent[w] = v;
                order.push_back(w);
            }
        }
    }

    // every dirt road joins an ancestor and a descendant;
    // it covers the stone roads on the path between them
    vector<int> cover(n + 1, 0);
    for (auto [a, b] : dirt) {
        if (depth[a] > depth[b]) swap(a, b);
        cover[b]++;
        cover[a]--;
    }
    for (int i = (int)order.size() - 1; i > 0; i--) cover[parent[order[i]]] += cover[order[i]];

    // a stone road covered by exactly one dirt road gives exactly one plan
    long long answer = 0;
    for (size_t i = 1; i < order.size(); i++)
        if (cover[order[i]] == 1) answer++;
    printf("%lld\n", answer);
}
