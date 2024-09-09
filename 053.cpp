#include "bits/stdc++.h"

using namespace std;
int main() {
    int n, m;
    cin >> n >> m;
    vector<int> a;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            a.push_back(i*j);
        }
    }
    int RED = 0, BLUE = 0, GREEN = 0;
    for (int &x : a) { if (x % 2 == 0 and x % 3 != 0 and x % 5 != 0) {RED++;}}
    for (int &x : a) { if (x % 3 == 0 and x % 5 != 0) {GREEN++;}}
    for (int &x : a) { if (x % 5 == 0) {BLUE++;}}
    int BLACK = n*m - GREEN - RED - BLUE;

    printf("RED : %d\nGREEN : %d\nBLUE : %d\nBLACK : %d", RED, GREEN, BLUE, BLACK);
    //system("pause");
}