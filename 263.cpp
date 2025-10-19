#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(nullptr);
    
    int N, i, j;
    if (!(cin >> N >> i >> j)) return 0;

    int cw  = (j - i + N) % N; 
    int ccw = (i - j + N) % N; 
    int edges = min(cw, ccw); 
    cout << edges - 1 << "\n"; 
    return 0;
}
