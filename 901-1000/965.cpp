#include <cstdio>

int main() {
    FILE* in = fopen("INPUT.TXT", "r");
    FILE* out = fopen("OUTPUT.TXT", "w");
    int n, m;
    fscanf(in, "%d %d", &n, &m);
    int adj[18] = {0};
    for (int i = 0; i < m; i++) {
        int u, v;
        fscanf(in, "%d %d", &u, &v);
        u--; v--;
        adj[u] |= 1 << v;
        adj[v] |= 1 << u;
    }
    int best = n + 1, count = 0, bestMask = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        int size = __builtin_popcount(mask);
        if (size > best) continue;
        bool ok = true;
        for (int v = 0; v < n && ok; v++)
            if (!(mask >> v & 1) && (adj[v] & ~mask)) ok = false;
        if (!ok) continue;
        if (size < best) {
            best = size;
            count = 1;
            bestMask = mask;
        } else {
            count++;
        }
    }
    fprintf(out, "%d %d\n", best, count);
    bool first = true;
    for (int v = 0; v < n; v++)
        if (bestMask >> v & 1) {
            fprintf(out, first ? "%d" : " %d", v + 1);
            first = false;
        }
    fprintf(out, "\n");
    return 0;
}
