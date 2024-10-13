#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <assert.h>
#include <chrono>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <random>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <variant>
#include <vector>
#include <queue>
#define logl log
#define expl exp
  
using namespace std;
  
const long long MOD = 1e9 + 9;
int binpow1(long long a, int b, long long MD) {
    long long r = 1;
    while (b) {
        if (b & 1) {
            r = (r * a) % MD;
        }
        a = (a * a) % MD;
        b >>= 1;
    }
    return r;
}
  
double lg_pre[200], llg_pre[200];
  
struct tower {
    int id;
    int k;
    vector<int> tow, bb;
    tower(int id) : id(id), k{}, tow{} {};
    void read(istream& is) {
        cin >> k;
        tow.resize(k + 1);
        for (auto& e : tow) cin >> e;
        for (int i = 0; i < tow.size(); ++i) {
            if (tow[i] == 1) {
                while (tow.size() > i) tow.pop_back();
                break;
            }
        }
  
        while (tow.size() > 1) {
            if (log(tow[tow.size() - 2]) * tow.back() > log(100)) break;
            int z = binpow1(tow[tow.size() - 2], tow.back(), MOD);
            if (z > 100) break;
            tow.pop_back();
            tow.back() = z;
        }
  
        if (tow.size() < 1)
            tow.push_back(1);
  
        bb.resize(tow.size() + 1);
        bb[tow.size() - 1] = tow.back();
  
        int w = tow.back();
  
        for (int i = tow.size() - 2; i > -1; --i) {
            bb[i] = binpow1(tow[i], w, MOD);
            w = binpow1(tow[i], w, MOD - 1);
        }
    }
  
    friend istream& operator>>(istream& is, tower& t) {
        t.read(is);
        return is;
    }
  
    bool breakdown(const tower& t, int k) const {
        for (; k > -1; --k) {
            if (tow[k] != t.tow[k]) {
                return tow[k] < t.tow[k];
            }
        }
        exit(-1);
    }
  
    bool operator<(tower& t) {
        if (tow.size() < t.tow.size()) {
            return !(t < *this);
        }
  
        if (tow.size() - t.tow.size() > 1) {
            return false;
        }
  
        if (tow.size() - t.tow.size() == 1) {
            t.tow.push_back(1);
            bool r = *this < t;
            t.tow.pop_back();
            return r;
        }
  
        if (!t.tow.size()) {
            return !tow.size();
        }
  
        int sz = tow.size();
  
        if (sz == 1) {
            return tow.back() < t.tow.back();
        }
  
        if (tow.size() == 2) {
            return tow.back() * logl(tow[sz - 2]) < t.tow.back() * log(t.tow[sz - 2]);
        }
  
        if (tow.size() == 3) {
            return tow.back() * logl(tow[sz - 2]) + logl(logl(tow[sz - 3])) < t.tow.back() * logl(t.tow[sz - 2]) + logl(logl(t.tow[sz - 3]));
        }
  
        if (10 * tow.back() <= t.tow.back()) {
            return true;
        }
  
        if (tow.back() >= 10 * t.tow.back()) {
            return false;
        }
  
        double log_1 = tow.back() * logl(tow[sz - 2]) - t.tow.back() * logl(t.tow[sz - 2]);
        if (log_1 >= logl(10)) {
            return false;
        }
  
        if (log_1 <= -logl(10)) {
            return true;
        }
  
        int k = sz - 2;
        int B1 = tow.back(), B2 = t.tow.back();
        while (k > -1) {
            if (bb[k] == t.bb[k]) {
                return breakdown(t, k - 1);
            }
            --k;
        }
        double a1 = lg_pre[tow[sz - 1]] + llg_pre[tow[sz - 2]];
        double a2 = lg_pre[t.tow[sz - 1]] + llg_pre[t.tow[sz - 2]];
        for (int dist = 3; dist <= sz; ++dist) {
            a1 = llg_pre[tow[sz - dist]] + expl(a1);
            a2 = llg_pre[t.tow[sz - dist]] + expl(a2);
  
            if (sz == dist) {
                return a1 < a2;
            }
  
            if (a1 - a2 >= 5) {
                return false;
            }
  
            if (a2 - a1 >= 5) {
                return true;
            }
  
            if (a1 >= a2 && logl(expl(a1 - a2) - 1) + a2 >= logl(logl(10))) {
                return false;
            }
  
            if (a2 >= a1 && logl(expl(a2 - a1) - 1) + a1 >= logl(logl(10))) {
                return true;
            }
        }
  
        exit(-1);
    }
  
};
  
signed main() {
    for (int i = 1; i <= 101; ++i) lg_pre[i] = logl(i), llg_pre[i] = logl(lg_pre[i]);
    int n;
    cin >> n;
    vector<tower> t;
    t.reserve(n);
    for (int i = 0; i < n; ++i) {
        t.emplace_back(i + 1);
        cin >> t[i];
    }
    sort(t.begin(), t.end());
    for (auto& e : t) cout << e.id << " ";
}