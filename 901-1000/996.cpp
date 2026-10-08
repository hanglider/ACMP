#include <iostream>
#include <set>
#include <unordered_set>

using namespace std;

int n, b, i;
unordered_set <int> t;

int main() {
    cin >> n;
    b = 1;
    t.insert(b);
    for (i = 2; i <= n; i++) {
        b += 2;
        if (t.find(i) != t.end())
            b++;
        t.insert(b);
    }
    cout << b;
    return 0;
}