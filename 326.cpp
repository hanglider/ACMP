#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    ifstream in("input.txt");
    int n, mx = 0, v = 105;
    in >> n;
    vector<int> a(n);
    int c[205] = {};
    for (int &x : a) {
        in >> x;
        int f = ++c[x + 100];
        if (f > mx || (f == mx && x < v)) mx = f, v = x;
    }
    int k = 0;
    for (int x : a) {
        if (x != v) cout << x << " ";
        else ++k;
    }
    while (k--) cout << v << " ";
    cout << '\n';
}
