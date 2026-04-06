#include <bits/stdc++.h>
using namespace std;

struct Player {
    int a1, a2, a3;
};

const long double EPSR = 1e-14L;
const long double EPSV = 1e-10L;

long double eval(const Player& x, long double p) {
    return (long double)x.a1 * p * p + (long double)x.a2 * p + (long double)x.a3;
}

vector<int> get_rank_vector(const vector<Player>& a, long double p) {
    int n = (int)a.size();
    vector<pair<long double, int>> v;
    v.reserve(n);
    for (int i = 0; i < n; ++i) v.push_back({eval(a[i], p), i});

    sort(v.begin(), v.end(), [](const auto& x, const auto& y) {
        if (fabsl(x.first - y.first) > EPSV) return x.first > y.first;
        return x.second < y.second;
    });

    vector<int> rank(n);
    int pos = 1;
    for (int l = 0; l < n; ) {
        int r = l;
        while (r + 1 < n && fabsl(v[r + 1].first - v[l].first) <= EPSV) ++r;
        for (int i = l; i <= r; ++i) rank[v[i].second] = pos;
        pos += r - l + 1;
        l = r + 1;
    }
    return rank;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<Player> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].a1 >> a[i].a2 >> a[i].a3;

    vector<long double> roots;

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            long double A = (long double)a[i].a1 - a[j].a1;
            long double B = (long double)a[i].a2 - a[j].a2;
            long double C = (long double)a[i].a3 - a[j].a3;

            if (fabsl(A) <= EPSR) {
                if (fabsl(B) <= EPSR) continue;
                long double x = -C / B;
                if (x > EPSR && x < 1.0L - EPSR) roots.push_back(x);
                else if (fabsl(x - 1.0L) <= EPSR) roots.push_back(1.0L);
            } else {
                long double D = B * B - 4.0L * A * C;
                if (D < -EPSR) continue;
                if (D < 0) D = 0;
                long double s = sqrtl(D);

                long double x1 = (-B - s) / (2.0L * A);
                long double x2 = (-B + s) / (2.0L * A);

                if (x1 > EPSR && x1 < 1.0L - EPSR) roots.push_back(x1);
                else if (fabsl(x1 - 1.0L) <= EPSR) roots.push_back(1.0L);

                if (fabsl(x2 - x1) > EPSR) {
                    if (x2 > EPSR && x2 < 1.0L - EPSR) roots.push_back(x2);
                    else if (fabsl(x2 - 1.0L) <= EPSR) roots.push_back(1.0L);
                }
            }
        }
    }

    sort(roots.begin(), roots.end());
    vector<long double> crit;
    for (long double x : roots) {
        if (crit.empty() || fabsl(x - crit.back()) > EPSR) crit.push_back(x);
    }

    vector<long double> points;
    long double prev = 0.0L;
    for (long double x : crit) {
        if (x - prev > EPSR) points.push_back((prev + x) / 2.0L);
        points.push_back(x);
        prev = x;
    }
    if (1.0L - prev > EPSR) points.push_back((prev + 1.0L) / 2.0L);
    if (points.empty()) points.push_back(0.5L);

    set<vector<int>> ans;
    for (long double p : points) ans.insert(get_rank_vector(a, p));

    cout << ans.size() << '\n';
    return 0;
}