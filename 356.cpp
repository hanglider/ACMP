#include <iostream>
using namespace std;
long long i,j,n, e, f, p[1000], w[1000],m1[10000],m2[10000];

int main() {
	cin >> e >> f >> n;
	f -= e;
	for (i = 0; i < n; i++)
		cin >> p[i] >> w[i];
	
	for (i = 0; i < n; i++) 
		m1[w[i]] = max(m1[w[i]],p[i]);
	
	for (i = 1; i < f; i++)
		if (m1[i] > 0) {
			for (j = 0; j < n; j++)
				if (i+w[j]<=f)
					m1[w[j] + i] = max(m1[w[j] + i], m1[i] + p[j]);
		}

	for (i = 0; i < n; i++)
		if (m2[w[i]] > 0)
			m2[w[i]] = min(m2[w[i]],p[i]);
		else m2[w[i]] = p[i];

	for (i = 1; i < f; i++)
		if (m2[i] > 0) {
			for (j = 0; j < n; j++)
				if (i + w[j] <= f) {
					if (m2[w[j] + i] > 0)
						m2[w[j] + i] = min(m2[w[j] + i], m2[i] + p[j]);
					else m2[w[j] + i] = m2[i] + p[j];
				}
		}
	if ((m1[f] == 0 || m2[f] == 0) && f>0)
		cout << "This is impossible.";
	else cout << m2[f] << " " << m1[f];
	return 0;
}