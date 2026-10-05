#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>
using namespace std;

int main() {
    double R, K;
    int n;
    if (scanf("%lf %lf %d", &R, &K, &n) != 3) n = 0;
    // cut the region along the ray above the head: a hair is a chord between
    // the shoulders (ordered by x) and the head (ordered by clockwise angle from the top);
    // two hairs cross iff both orders agree
    vector<pair<double, double>> hair(n);  // (x on shoulders, angle on head)
    for (int i = 0; i < n; i++) {
        double xh, yh, xs, ys;
        if (scanf("%lf %lf %lf %lf", &xh, &yh, &xs, &ys) != 4) break;
        double t = atan2(xh, yh);
        if (t < 0) t += 2 * acos(-1.0);
        hair[i] = {xs, t};
    }
    vector<double> angles(n);
    for (int i = 0; i < n; i++) angles[i] = hair[i].second;
    sort(angles.begin(), angles.end());
    sort(hair.begin(), hair.end());
    vector<int> bit(n + 1, 0);
    long long answer = 0;
    for (int i = 0; i < n; i++) {
        int r = lower_bound(angles.begin(), angles.end(), hair[i].second) - angles.begin() + 1;
        for (int j = r - 1; j > 0; j -= j & -j) answer += bit[j];
        for (int j = r; j <= n; j += j & -j) bit[j]++;
    }
    printf("%lld\n", answer);
}
