#include <cstdio>
#include <cstdlib>
#include <algorithm>

int main() {
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);
    int ys[10], xs[10];
    for (int i = 0; i < k; i++)
        scanf("%d %d", &ys[i], &xs[i]);
    int answer = 0;
    for (int y = 1; y <= n; y++) {
        for (int x = 1; x <= m; x++) {
            int best = 1 << 30;
            for (int i = 0; i < k; i++)
                best = std::min(best, abs(y - ys[i]) + abs(x - xs[i]));
            answer = std::max(answer, best);
        }
    }
    printf("%d\n", answer);
    return 0;
}
