#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> magicOdd(int n) {
    vector<vector<int>> a(n, vector<int>(n, 0));
    int i = 0, j = n / 2;
    for (int num = 1; num <= n * n; ++num) {
        a[i][j] = num;
        int ni = (i - 1 + n) % n;
        int nj = (j + 1) % n;
        if (a[ni][nj]) i = (i + 1) % n;
        else { i = ni; j = nj; }
    }
    return a;
}

vector<vector<int>> magicDoubleEven(int n) {
    vector<vector<int>> a(n, vector<int>(n));
    int num = 1;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            a[i][j] = num++;

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if ((i % 4 == j % 4) || ((i % 4) + (j % 4) == 3))
                a[i][j] = n * n + 1 - a[i][j];
    return a;
}

vector<vector<int>> magicSinglyEven(int n) {
    int m = n / 2;                 
    int t = m * m;

    auto base = magicOdd(m);

    vector<vector<int>> A(m, vector<int>(m)), B=A, C=A, D=A;
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < m; ++j) {
            A[i][j] = base[i][j];
            B[i][j] = base[i][j] + t;
            C[i][j] = base[i][j] + 2*t;
            D[i][j] = base[i][j] + 3*t;
        }

    vector<vector<int>> a(n, vector<int>(n));
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < m; ++j) {
            a[i][j]       = A[i][j];
            a[i][j + m]   = C[i][j];
            a[i + m][j]   = D[i][j];
            a[i + m][j+m] = B[i][j];
        }

    int k = (n - 2) / 4; 

    for (int i = 0; i < m; ++i)
        for (int j = 0; j < k; ++j)
            swap(a[i][j], a[i + m][j]);

    if (k - 1 > 0) {
        for (int i = 0; i < m; ++i)
            for (int j = m - (k - 1); j < m; ++j) 
                swap(a[i][j + m], a[i + m][j + m]);
    }

    int midRow = m / 2;
    swap(a[midRow][0], a[midRow + m][0]);         
    swap(a[midRow][midRow], a[midRow + m][midRow]); 

    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    if (N == 2) {
        cout << "Impossible";
        return 0;
    }

    vector<vector<int>> res;
    if (N % 2 == 1) res = magicOdd(N);
    else if (N % 4 == 0) res = magicDoubleEven(N);
    else res = magicSinglyEven(N); 

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (j) cout << ' ';
            cout << res[i][j];
        }
        cout << '\n';
    }
    return 0;
}
