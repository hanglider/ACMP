#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

// A circle crosses the interior of a segment exactly once iff one endpoint
// is strictly inside the circle and the other one is strictly outside.
// So we choose which endpoint of each segment is inside and look for a
// center c maximizing  min dist(c, outside) - max dist(c, inside).

struct Pt { double x, y; };

const double BOX = 1e7;
const double PI = acos(-1.0);

Pt inPts[2], outPts[2];

double margin(Pt c) {
    double inMax = 0, outMin = 1e300;
    for (int i = 0; i < 2; i++) {
        inMax = max(inMax, hypot(c.x - inPts[i].x, c.y - inPts[i].y));
        outMin = min(outMin, hypot(c.x - outPts[i].x, c.y - outPts[i].y));
    }
    return outMin - inMax;
}

// keep points p with a*p.x + b*p.y < c
vector<Pt> clip(const vector<Pt>& poly, double a, double b, double c) {
    vector<Pt> res;
    int n = poly.size();
    for (int i = 0; i < n; i++) {
        Pt p = poly[i], q = poly[(i + 1) % n];
        double vp = a * p.x + b * p.y - c, vq = a * q.x + b * q.y - c;
        if (vp < 0) res.push_back(p);
        if ((vp < 0) != (vq < 0)) {
            double t = vp / (vp - vq);
            res.push_back({p.x + (q.x - p.x) * t, p.y + (q.y - p.y) * t});
        }
    }
    return res;
}

void climb(Pt& c, double& best, double step) {
    // pattern search over 16 directions with a rotating offset,
    // so it can follow the ridges of the non-smooth margin function
    double phase = 0;
    for (int iter = 0; iter < 300 && step > 1e-6; iter++) {
        bool moved = false;
        phase += 0.618;
        for (int d = 0; d < 16; d++) {
            double ang = phase + d * PI / 8;
            Pt q = {c.x + cos(ang) * step, c.y + sin(ang) * step};
            if (fabs(q.x) > BOX || fabs(q.y) > BOX) continue;
            double v = margin(q);
            if (v > best) {
                best = v;
                c = q;
                moved = true;
                break;
            }
        }
        if (moved) step *= 1.5;
        else step /= 2;
    }
}

int main() {
    freopen("INPUT.TXT", "r", stdin);
    freopen("OUTPUT.TXT", "w", stdout);
    int s[2][4];
    while (true) {
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 4; j++)
                if (scanf("%d", &s[i][j]) != 1) return 0;
        bool allZero = true;
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 4; j++)
                if (s[i][j] != 0) allZero = false;
        if (allZero) break;

        Pt end[2][2];
        for (int i = 0; i < 2; i++) {
            end[i][0] = {(double)s[i][0], (double)s[i][1]};
            end[i][1] = {(double)s[i][2], (double)s[i][3]};
        }

        double bestMargin = -1e300;
        Pt bestCenter = {0, 0};
        Pt bestIn[2], bestOut[2];
        for (int mask = 0; mask < 4; mask++) {
            for (int i = 0; i < 2; i++) {
                int k = (mask >> i) & 1;
                inPts[i] = end[i][k];
                outPts[i] = end[i][1 - k];
            }
            vector<Pt> poly = {{-BOX, -BOX}, {BOX, -BOX}, {BOX, BOX}, {-BOX, BOX}};
            for (int i = 0; i < 2 && !poly.empty(); i++)
                for (int j = 0; j < 2 && !poly.empty(); j++) {
                    Pt p = inPts[i], q = outPts[j];
                    double a = 2 * (q.x - p.x), b = 2 * (q.y - p.y);
                    double c = q.x * q.x + q.y * q.y - p.x * p.x - p.y * p.y;
                    if (a == 0 && b == 0) { poly.clear(); break; }
                    poly = clip(poly, a, b, c);
                }
            if (poly.size() < 3) continue;

            Pt avg = {0, 0};
            for (Pt p : poly) { avg.x += p.x; avg.y += p.y; }
            avg.x /= poly.size();
            avg.y /= poly.size();
            double diam = 0;
            for (Pt p : poly) diam = max(diam, hypot(p.x - avg.x, p.y - avg.y));

            // candidate centers: points inside the feasible polygon, a coarse grid
            // around the segments and far points (circles close to straight lines)
            vector<Pt> seeds = {avg};
            for (Pt p : poly) seeds.push_back({(p.x + avg.x) / 2, (p.y + avg.y) / 2});
            for (int gx = -120; gx <= 120; gx += 15)
                for (int gy = -120; gy <= 120; gy += 15)
                    seeds.push_back({(double)gx, (double)gy});
            // the endpoints themselves and the midpoints between them
            Pt all[4] = {inPts[0], inPts[1], outPts[0], outPts[1]};
            for (int i = 0; i < 4; i++)
                for (int j = i; j < 4; j++)
                    seeds.push_back({(all[i].x + all[j].x) / 2, (all[i].y + all[j].y) / 2});
            for (int d = 0; d < 64; d++)
                seeds.push_back({1e6 * cos(d * PI / 32), 1e6 * sin(d * PI / 32)});
            Pt c = seeds[0];
            double v = margin(c);
            for (Pt seed : seeds) {
                double w = margin(seed);
                if (w > v) { v = w; c = seed; }
            }
            // refine only when the candidates give a poor margin
            if (v < 0.05 && bestMargin < 0.05) climb(c, v, min(max(diam / 4, 1e-6), 10.0));
            if (v > bestMargin) {
                bestMargin = v;
                bestCenter = c;
                bestIn[0] = inPts[0]; bestIn[1] = inPts[1];
                bestOut[0] = outPts[0]; bestOut[1] = outPts[1];
            }
        }

        inPts[0] = bestIn[0]; inPts[1] = bestIn[1];
        outPts[0] = bestOut[0]; outPts[1] = bestOut[1];
        Pt c = bestCenter;
        double inMax = max(hypot(c.x - inPts[0].x, c.y - inPts[0].y), hypot(c.x - inPts[1].x, c.y - inPts[1].y));
        double outMin = min(hypot(c.x - outPts[0].x, c.y - outPts[0].y), hypot(c.x - outPts[1].x, c.y - outPts[1].y));
        printf("%.10f %.10f %.10f\n", c.x, c.y, (inMax + outMin) / 2);
    }
    return 0;
}
