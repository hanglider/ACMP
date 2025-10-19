#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int to, rev, cap;
    int cost;
    Edge(int _to, int _rev, int _cap, int _cost)
        : to(_to), rev(_rev), cap(_cap), cost(_cost) {}
};

struct MinCostMaxFlow {
    int n;
    vector<vector<Edge>> g;
    MinCostMaxFlow(int n): n(n), g(n) {}

    void addEdge(int u, int v, int cap, int cost) {
        Edge a(v, (int)g[v].size(), cap, cost);
        Edge b(u, (int)g[u].size(), 0, -cost);
        g[u].push_back(a);
        g[v].push_back(b);
    }

    pair<int,long long> minCostMaxFlow(int s, int t) {
        const long long INF = (1LL<<60);
        long long cost = 0;
        int flow = 0;
        vector<long long> pot(n, 0); 

        while (true) {
            vector<long long> dist(n, INF);
            vector<int> pv_v(n, -1), pv_e(n, -1);
            priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;

            dist[s] = 0;
            pq.push({0, s});

            while (!pq.empty()) {
                auto [d, v] = pq.top(); pq.pop();
                if (d != dist[v]) continue;
                for (int ei = 0; ei < (int)g[v].size(); ++ei) {
                    const Edge &e = g[v][ei];
                    if (e.cap <= 0) continue;
                    long long nd = d + e.cost + pot[v] - pot[e.to];
                    if (nd < dist[e.to]) {
                        dist[e.to] = nd;
                        pv_v[e.to] = v;
                        pv_e[e.to] = ei;
                        pq.push({nd, e.to});
                    }
                }
            }
            if (dist[t] == INF) break;

            for (int v = 0; v < n; ++v)
                if (dist[v] < INF) pot[v] += dist[v];

            int add = INT_MAX;
            for (int v = t; v != s; v = pv_v[v]) {
                Edge &e = g[pv_v[v]][pv_e[v]];
                add = min(add, e.cap);
            }
            for (int v = t; v != s; v = pv_v[v]) {
                Edge &e = g[pv_v[v]][pv_e[v]];
                Edge &re = g[e.to][e.rev];
                e.cap -= add;
                re.cap += add;
            }
            flow += add;
            cost += (long long)add * pot[t];
        }
        return {flow, cost};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    vector<int> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];

    int source = N;       
    int sink   = N + 1;   
    MinCostMaxFlow mcmf(N + 2);

    const int INF_CAP = 1e9;
    for (int i = 0; i < N; ++i) {
        int j = (i + 1) % N;
        mcmf.addEdge(i, j, INF_CAP, 1);
        mcmf.addEdge(j, i, INF_CAP, 1);
    }

    int total_excess = 0;

    for (int i = 0; i < N; ++i) {
        if (A[i] >= 2) {
            int excess = A[i] - 1;
            mcmf.addEdge(source, i, excess, 0);
            total_excess += excess;
        }
    }

    for (int i = 0; i < N; ++i) {
        if (A[i] == 0) {
            mcmf.addEdge(i, sink, 1, 0);
        }
    }

    auto [flow, minCost] = mcmf.minCostMaxFlow(source, sink);

    cout << minCost << "\n";
    return 0;
}
