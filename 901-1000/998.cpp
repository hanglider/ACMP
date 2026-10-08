#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>
using namespace std;

const double PI = acos(-1.0);
double d, r, x1, y1_, x2, y2_, u, v;
double homeAngle, schoolAngle;

// angular distance along the circle between two angles
double arc(double a, double b) {
    double diff = fmod(fabs(a - b), 2 * PI);
    return min(diff, 2 * PI - diff);
}

// ride along the home track to angle a, cross the field to angle b on the school track,
// then ride along the school track to the school
double travelTime(double a, double b) {
    double ax = r * cos(a), ay = r * sin(a);
    double bx = r * cos(b), by = d + r * sin(b);
    double field = hypot(ax - bx, ay - by);
    return (arc(homeAngle, a) + arc(b, schoolAngle)) * r / u + field / v;
}

double bestOverB(double a, double lo, double hi) {
    for (int it = 0; it < 100; it++) {
        double m1 = lo + (hi - lo) / 3, m2 = hi - (hi - lo) / 3;
        if (travelTime(a, m1) < travelTime(a, m2)) hi = m2; else lo = m1;
    }
    return travelTime(a, (lo + hi) / 2);
}

double refine(double a0, double b0, double h) {
    double lo = a0 - h, hi = a0 + h;
    for (int it = 0; it < 100; it++) {
        double m1 = lo + (hi - lo) / 3, m2 = hi - (hi - lo) / 3;
        if (bestOverB(m1, b0 - h, b0 + h) < bestOverB(m2, b0 - h, b0 + h)) hi = m2; else lo = m1;
    }
    return bestOverB((lo + hi) / 2, b0 - h, b0 + h);
}

int main() {
    if (scanf("%lf %lf %lf %lf %lf %lf %lf %lf", &d, &r, &x1, &y1_, &x2, &y2_, &u, &v) != 8) return 0;
    homeAngle = atan2(y1_, x1);
    schoolAngle = atan2(y2_ - d, x2);

    const int G = 1000;
    double step = 2 * PI / G;
    vector<pair<double, pair<int, int>>> cells;
    cells.reserve((size_t)G * G);
    for (int i = 0; i < G; i++)
        for (int j = 0; j < G; j++)
            cells.push_back({travelTime(i * step, j * step), {i, j}});
    const int K = 30;
    partial_sort(cells.begin(), cells.begin() + K, cells.end());

    double best = travelTime(homeAngle, schoolAngle);
    for (int k = 0; k < K; k++) {
        best = min(best, cells[k].first);
        best = min(best, refine(cells[k].second.first * step, cells[k].second.second * step, 2 * step));
    }
    printf("%.10f\n", best);
}
