#include <iostream>
#include <string>
using namespace std;
int i, n, sum, a[24], znak[24],flag;
string s;
void rec(int ind, int tek) {
  if (flag == 0) {
      if (tek == sum) {
          flag = 1;
          for (i = 0; i < n; i++) {
              if (znak[i] == 0)
                  s += "+";
              else s += "-";
              s += to_string(a[i]);
          }
          s.erase(0, 1);
          cout << s + "=" << sum;
      }
      else if (ind < n) {
        znak[ind] = 0;
        rec(ind + 1, tek + a[ind]);
        znak[ind] = 1;
        rec(ind + 1, tek - a[ind]);
      }
  }
}
 
int main()
{
    cin >> n >> sum;
    for (i = 0; i < n; i++)
        cin >> a[i];
     
    rec(1, a[0]);
 
    if (s == "") 
     cout << "No solution";
    return 0;
}