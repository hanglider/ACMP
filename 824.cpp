#include <bits/stdc++.h>
using namespace std;
struct B {
    int s;
    vector<int> d;
};
B mk(long long x) {
    B r;
    r.s = x < 0 ? -1 : (x > 0 ? 1 : 0);
    x = llabs(x);
    if (x == 0)
        r.d.push_back(0);
    while (x) {
        r.d.push_back(x % 10);
        x /= 10;
    }
    return r;
}
void trim(B &a) {
    while (a.d.size() > 1 && a.d.back() == 0)
        a.d.pop_back();
    if (a.d.size() == 1 && a.d[0] == 0)
        a.s = 0;
}
int cmpAbs(const B &a, const B &b) {
    if (a.d.size() != b.d.size())
        return a.d.size() < b.d.size() ? -1 : 1;
    for (int i = (int)a.d.size() - 1; i >= 0; i--)
        if (a.d[i] != b.d[i])
            return a.d[i] < b.d[i] ? -1 : 1;
    return 0;
}
B addAbs(const B &a, const B &b) {
    B r;
    r.s = 1;
    int n = max(a.d.size(), b.d.size());
    int carry = 0;
    for (int i = 0; i < n || carry; i++) {
        int x = carry;
        if (i < (int)a.d.size())
            x += a.d[i];
        if (i < (int)b.d.size())
            x += b.d[i];
        r.d.push_back(x % 10);
        carry = x / 10;
    }
    trim(r);
    return r;
}
B subAbs(const B &a, const B &b) {
    B r;
    r.s = 1;
    int borrow = 0;
    for (int i = 0; i < (int)a.d.size(); i++) {
        int x = a.d[i] - borrow - (i < (int)b.d.size() ? b.d[i] : 0);
        if (x < 0) {
            x += 10;
            borrow = 1;
        } else
            borrow = 0;
        r.d.push_back(x);
    }
    trim(r);
    return r;
}
B operator+(const B &a, const B &b) {
    if (a.s == 0)
        return b;
    if (b.s == 0)
        return a;
    if (a.s == b.s) {
        B r = addAbs(a, b);
        r.s = a.s;
        return r;
    }
    int c = cmpAbs(a, b);
    if (c == 0)
        return mk(0);
    if (c > 0) {
        B r = subAbs(a, b);
        r.s = a.s;
        return r;
    }
    B r = subAbs(b, a);
    r.s = b.s;
    return r;
}
B neg(B a) {
    a.s = -a.s;
    return a;
}
B operator-(const B &a, const B &b) {
    return a + neg(b);
}
B operator*(const B &a, const B &b) {
    if (a.s == 0 || b.s == 0)
        return mk(0);
    vector<long long> t(a.d.size() + b.d.size(), 0);
    for (int i = 0; i < (int)a.d.size(); i++)
        for (int j = 0; j < (int)b.d.size(); j++)
            t[i + j] += (long long)a.d[i] * b.d[j];
    long long carry = 0;
    B r;
    r.s = a.s * b.s;
    for (int i = 0; i < (int)t.size() || carry; i++) {
        long long x = carry + (i < (int)t.size() ? t[i] : 0);
        r.d.push_back(x % 10);
        carry = x / 10;
    }
    trim(r);
    return r;
}
B divExact(const B &a, const B &b) {
    if (a.s == 0)
        return mk(0);
    B cur = mk(0);
    B q;
    q.s = 1;
    q.d.assign(a.d.size(), 0);
    for (int i = (int)a.d.size() - 1; i >= 0; i--) {
        cur.d.insert(cur.d.begin(), a.d[i]);
        trim(cur);
        int lo = 0, hi = 9, best = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            B bb;
            bb.s = 1;
            bb.d.push_back(mid);
            B pr = b;
            pr.s = 1;
            B prod = pr * bb;
            if (cmpAbs(prod, cur) <= 0) {
                best = mid;
                lo = mid + 1;
            } else
                hi = mid - 1;
        }
        q.d[i] = best;
        B bb;
        bb.s = 1;
        bb.d.push_back(best);
        B pr = b;
        pr.s = 1;
        cur = subAbs(cur, pr * bb);
    }
    trim(q);
    q.s = (q.d.size() == 1 && q.d[0] == 0) ? 0 : a.s * b.s;
    return q;
}
string toStr(const B &a) {
    string r;
    if (a.s < 0)
        r += "-";
    for (int i = (int)a.d.size() - 1; i >= 0; i--)
        r += char('0' + a.d[i]);
    return r;
}
int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> w(n, vector<int>(n, 0));
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        w[a][b]++;
        w[b][a]++;
    }
    int sz = n - 1;
    vector<vector<B>> mat(sz, vector<B>(sz));
    for (int i = 0; i < sz; i++) {
        for (int j = 0; j < sz; j++) {
            if (i == j) {
                int deg = 0;
                for (int k = 0; k < n; k++)
                    deg += w[i][k];
                mat[i][j] = mk(deg);
            } else {
                mat[i][j] = mk(-w[i][j]);
            }
        }
    }
    B prev = mk(1);
    for (int k = 0; k < sz - 1; k++) {
        for (int i = k + 1; i < sz; i++) {
            for (int j = k + 1; j < sz; j++) {
                B val = mat[i][j] * mat[k][k] - mat[i][k] * mat[k][j];
                mat[i][j] = divExact(val, prev);
            }
        }
        prev = mat[k][k];
    }
    if (sz == 0)
        cout << 1;
    else
        cout << toStr(mat[sz - 1][sz - 1]);
}
