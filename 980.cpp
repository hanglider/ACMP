#include <bits/stdc++.h>
using namespace std;

// Chain decomposition (Schmidt): chains in DFS preorder form an ear
// decomposition of a 2-edge-connected graph; cutting them in reverse order works.
int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2) return 0;
    vector<int> eu(m), ev(m);
    vector<vector<pair<int, int>>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        if (scanf("%d %d", &eu[i], &ev[i]) != 2) return 0;
        adj[eu[i]].push_back({ev[i], i});
        adj[ev[i]].push_back({eu[i], i});
    }
    vector<int> pre(n + 1, -1), parent(n + 1, 0), parentEdge(n + 1, -1), order;
    vector<size_t> it(n + 1, 0);
    vector<int> st = {1};
    pre[1] = 0;
    order.push_back(1);
    while (!st.empty()) {
        int v = st.back();
        if (it[v] < adj[v].size()) {
            auto [w, e] = adj[v][it[v]++];
            if (pre[w] == -1) {
                pre[w] = order.size();
                order.push_back(w);
                parent[w] = v;
                parentEdge[w] = e;
                st.push_back(w);
            }
        } else {
            st.pop_back();
        }
    }
    vector<char> isTree(m, 0);
    for (int v = 2; v <= n; v++) isTree[parentEdge[v]] = 1;
    vector<vector<int>> backFrom(n + 1);  // ancestor -> descendants via back edges
    for (int i = 0; i < m; i++) {
        if (isTree[i]) continue;
        int a = eu[i], b = ev[i];
        if (pre[a] > pre[b]) swap(a, b);
        backFrom[a].push_back(b);
    }
    vector<char> visited(n + 1, 0);
    vector<vector<int>> chains;
    long long covered = 0;
    for (int v : order) {
        for (int w : backFrom[v]) {
            visited[v] = 1;
            vector<int> chain = {v};
            int x = w;
            while (true) {
                chain.push_back(x);
                if (visited[x]) break;
                visited[x] = 1;
                x = parent[x];
            }
            covered += chain.size() - 1;
            chains.push_back(chain);
        }
    }
    if (covered != m) {
        printf("-1\n");
        return 0;
    }
    string out = to_string(chains.size()) + "\n";
    for (int i = (int)chains.size() - 1; i >= 0; i--) {
        out += to_string(chains[i].size() - 1);
        for (int x : chains[i]) out += " " + to_string(x);
        out += "\n";
    }
    fputs(out.c_str(), stdout);
}
