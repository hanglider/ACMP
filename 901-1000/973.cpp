#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

typedef long long ll;
const ll INF = (ll)4e18;

int n, m;
vector<int> eu, ev, ew;
vector<vector<int>> adj;  // edge indices

vector<ll> dijkstra(int src) {
    vector<ll> dist(n + 1, INF);
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> pq;
    dist[src] = 0;
    pq.push({0, src});
    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (d > dist[u]) continue;
        for (int e : adj[u]) {
            int v = eu[e] == u ? ev[e] : eu[e];
            if (d + ew[e] < dist[v]) {
                dist[v] = d + ew[e];
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}

int main() {
    FILE* in = fopen("INPUT.TXT", "r");
    FILE* out = fopen("OUTPUT.TXT", "w");
    if (fscanf(in, "%d %d", &n, &m) != 2) return 0;
    eu.resize(m); ev.resize(m); ew.resize(m);
    adj.assign(n + 1, {});
    for (int i = 0; i < m; i++) {
        if (fscanf(in, "%d %d %d", &eu[i], &ev[i], &ew[i]) != 3) return 0;
        adj[eu[i]].push_back(i);
        adj[ev[i]].push_back(i);
    }
    vector<ll> d1 = dijkstra(1), dn = dijkstra(n);
    ll total = d1[n];

    // every shortest-path edge covers the distance interval [d1[from], d1[to]];
    // it is critical iff no other shortest-path edge overlaps that interval
    vector<int> spEdges;
    vector<ll> lo, hi;
    for (int i = 0; i < m; i++) {
        for (int dir = 0; dir < 2; dir++) {
            int a = dir ? ev[i] : eu[i], b = dir ? eu[i] : ev[i];
            if (d1[a] < INF && dn[b] < INF && d1[a] + ew[i] + dn[b] == total) {
                spEdges.push_back(i);
                lo.push_back(d1[a]);
                hi.push_back(d1[a] + ew[i]);
            }
        }
    }
    vector<ll> coords(lo.begin(), lo.end());
    coords.insert(coords.end(), hi.begin(), hi.end());
    sort(coords.begin(), coords.end());
    coords.erase(unique(coords.begin(), coords.end()), coords.end());
    int k = coords.size();
    vector<int> cover(k + 1, 0);  // cover[j]: number of intervals over (coords[j], coords[j+1])
    for (size_t i = 0; i < spEdges.size(); i++) {
        int a = lower_bound(coords.begin(), coords.end(), lo[i]) - coords.begin();
        int b = lower_bound(coords.begin(), coords.end(), hi[i]) - coords.begin();
        cover[a]++;
        cover[b]--;
    }
    for (int j = 1; j <= k; j++) cover[j] += cover[j - 1];

    vector<int> result;
    for (size_t i = 0; i < spEdges.size(); i++) {
        int a = lower_bound(coords.begin(), coords.end(), lo[i]) - coords.begin();
        int b = lower_bound(coords.begin(), coords.end(), hi[i]) - coords.begin();
        if (b == a + 1 && cover[a] == 1) result.push_back(spEdges[i] + 1);
    }
    sort(result.begin(), result.end());
    fprintf(out, "%d\n", (int)result.size());
    for (size_t i = 0; i < result.size(); i++) fprintf(out, "%s%d", i ? " " : "", result[i]);
    fprintf(out, "\n");
    return 0;
}
