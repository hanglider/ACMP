#include <iostream>
long long n, b;
main() {
    b = 1;
    std::cin >> n;
    while (b < n)
      b *= 2;
    std::cout << std::min(n - b/2, b - n);    
}