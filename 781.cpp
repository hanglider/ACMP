#include <iostream>
main() {
    int n, i, a,x;
    std::cin >> n;
    a = 2;
    x = 4;
    for (i = 2; i < n; i++) 
        std::swap(a, x), x += a;
    if (n==1)
        x=a;
    std::cout << x;
}