#include <bits/stdc++.h>

#define ll long long

using namespace std;

int main() {
  ll f, p;
  cin >> f >> p;
  if (f <= 0 || p < 0) {
    cout << 0 << endl;
    return 0;
  }
  if (p >= f) {
    cout << f << endl;
    return 0;
  }
  ll d = f - p;
  ll cur = 0;
  for (int i = 0; i < 4; ++i) {
    ll delta = cur + 1;
    ll low = (cur * f / p) + 1;
    ll high = (delta * f / p);
    ll chosen = -1;
    for (ll pk = low; pk <= high; ++pk) {
      ll temp = pk * d;
      ll q = temp / f;
      ll nextk = pk - 1 - q;
      if (nextk == cur) {
        chosen = pk;
        break;
      }
    }
    assert(chosen != -1); 
    cur = chosen;
  }
  ll ans = f + cur * d;
  cout << ans << endl;
  return 0;
}

