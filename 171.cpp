#include <iostream>
#include <cmath>
using namespace std;
long long n, i, j,k,nn,ans = 1, x, kol,t[1000];
int main() {
	cin >> nn;
	n = nn;

	for (i = 2; i < 1000; i++) {
		k = round(sqrt(i))+1;
		for (j = 2; j < k; j++)
			if (i % j == 0)
				break;
		
		if (j == k) {
			t[x] = i;
			x++;
		}
	}

	for (i = 0; i < x; i++) {
		kol = 0;
		while (n % t[i] == 0) {
			n /= t[i];
			kol++;
		}
		ans *= (kol + 1);
	}

	if (n > 1) {
		ans++;
		if (n != nn)
			ans++;
	}

	cout << ans;
	return 0;
}