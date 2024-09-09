#include "bits/stdc++.h"

using namespace std;

main() { 
    char c;
    int k = 0, m = 0; 
    while(cin >> c) 
        if(c == '0') { 
            k++; 
            if (k > m) m=k; 
        } 
        else k = 0; 
    cout << m; 
}