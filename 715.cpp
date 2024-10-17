#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <stack>

#define each(x, a) for (auto &x : a)
#define pb push_back

using ll = long long;
using namespace std;
int x, i, n, m, ans, j;
string s;
char a [100][100];
char b [100][100];

int main()
{
    cin >> n >> m;
    for (i = 0; i < n; i++){
        for (j = 0; j < m; j++){
            cin >> a[i][j];
        }
    }
    getline(cin , s);  
    for (i = 0; i < n; i++){
        for (j = 0; j < m; j++){
            cin >> b[i][j];
        }
    }
    
    for (i = 0; i < n; i++){
        for (j = 0; j < m; j++){
            if (a[i][j] == b[i][j]) ans += 1;
        }
    }
    cout << ans;
    return 0;
}
