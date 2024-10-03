#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a = {1, 2};
    for (int i = 1; i <= n; ++i){
        a.push_back(a.back() + i+1);
    }
    cout << a[n];
    return 0;
}