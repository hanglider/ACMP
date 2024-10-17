#include <iostream> 
#include <algorithm> 
#include <vector> 
#include <stdlib.h> 
#include <string>
#include <math.h>
 
using namespace std; 
 
int main() 
{ 
    string s;
    cin >> s;
    if (s == "6"){
        cout << 3;
        exit(0);
    }
    if (s == "2"){
        cout << 2;
        exit(0);
    }
    if (s == "1"){
        cout << 1;
        exit(0);
    }
    if (s == "720"){
        cout << 6;
        exit(0);
    }
    auto x = 0.0;
    int i = 0;
    while (ceil(x) != s.size()) {
        i++;
        x += log10(i);
    }
    cout << i;
    return 0;
}