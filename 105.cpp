#include <bits/stdc++.h>
using namespace std;
struct Node {
    bool lf;
    long long v;
    vector<Node> k;
};
struct Tok {
    int t;
    long long v;
};
vector<Tok> tk;
int p;
Node parseSeq() {
    Node n;
    n.lf = false;
    while (p < (int)tk.size() && tk[p].t != 2) {
        Node it;
        if (tk[p].t == 0) {
            it.lf = true;
            it.v = tk[p].v;
            p++;
        } else {
            p++;
            it = parseSeq();
            p++;
        }
        n.k.push_back(it);
    }
    return n;
}
int cnt(Node &n) {
    if (n.lf)
        return 0;
    int c = (int)n.k.size() - 1;
    for (auto &x : n.k)
        c += cnt(x);
    return c;
}
long long apl(long long a, int o, long long b) {
    if (o == 0)
        return a + b;
    if (o == 1)
        return a - b;
    return a * b;
}
vector<int> ops;
long long ev(Node &n, int &idx) {
    if (n.lf)
        return n.v;
    long long r = ev(n.k[0], idx);
    for (int i = 1; i < (int)n.k.size(); i++) {
        int o = ops[idx++];
        long long v2 = ev(n.k[i], idx);
        r = apl(r, o, v2);
    }
    return r;
}
char ch(int o) {
    return o == 0 ? '+' : o == 1 ? '-' : '*';
}
string bi(Node &n, int &idx);
string bg(Node &n, int &idx) {
    string r = bi(n.k[0], idx);
    for (int i = 1; i < (int)n.k.size(); i++) {
        int o = ops[idx++];
        r += ch(o);
        r += bi(n.k[i], idx);
    }
    return r;
}
string bi(Node &n, int &idx) {
    if (n.lf)
        return to_string(n.v);
    return "(" + bg(n, idx) + ")";
}
int main() {
    string line;
    getline(cin, line);
    int eq = line.find('=');
    long long target = stoll(line.substr(0, eq));
    string rest = line.substr(eq + 1);
    for (int i = 0; i < (int)rest.size(); i++) {
        char c = rest[i];
        if (c == ' ')
            continue;
        if (c == '(') {
            tk.push_back({1, 0});
            continue;
        }
        if (c == ')') {
            tk.push_back({2, 0});
            continue;
        }
        long long x = 0;
        while (i < (int)rest.size() && isdigit(rest[i])) {
            x = x * 10 + (rest[i] - '0');
            i++;
        }
        i--;
        tk.push_back({0, x});
    }
    p = 0;
    Node root = parseSeq();
    int slots = cnt(root);
    long long tot = 1;
    for (int i = 0; i < slots; i++)
        tot *= 3;
    for (long long m = 0; m < tot; m++) {
        ops.assign(slots, 0);
        long long mm = m;
        for (int i = 0; i < slots; i++) {
            ops[i] = mm % 3;
            mm /= 3;
        }
        int idx = 0;
        long long r = ev(root, idx);
        if (r == target) {
            int idx2 = 0;
            string s = bg(root, idx2);
            cout << target << "=" << s;
            return 0;
        }
    }
    cout << -1;
}
