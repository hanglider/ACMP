#include <iostream>
#include <queue>
using namespace std;

int mn=100,i, j, k, h, m, n, a[8][8], b[8][8];
pair <int, int> d[8];
pair<int, int> s, f, tek;
queue<pair<int, int>> q;
char c;
int main() {
	d[0] = make_pair(-2, 1);
	d[1] = make_pair(-1, 2);
	d[2] = make_pair(1, 2);
	d[3] = make_pair(2, 1);
	d[4] = make_pair(2, -1);
	d[5] = make_pair(1, -2);
	d[6] = make_pair(-1, -2);
	d[7] = make_pair(-2, -1);

	cin >> c >> s.second;
	s.first = int(c - 'a');
	s.second--;

	cin >> c >> f.second;
	f.first = int(c - 'a');
	f.second--;

	a[s.first][s.second] = 1;
	b[f.first][f.second] = 1;

	q.push(s);
	while (q.size() > 0) {
		tek = q.front();
		q.pop();

		for (i = 0; i < 8; i++)
			if (tek.first + d[i].first >= 0 && tek.second + d[i].second >= 0 && tek.first + d[i].first < 8 && tek.second + d[i].second < 8 && a[tek.first + d[i].first][tek.second + d[i].second] == 0) {
				a[tek.first + d[i].first][tek.second + d[i].second] = a[tek.first][tek.second] + 1;
				q.push(make_pair(tek.first + d[i].first, tek.second + d[i].second));
			}
	}

	q.push(f);
	while (q.size() > 0) {
		tek = q.front();
		q.pop();

		for (i = 0; i < 8; i++)
			if (tek.first + d[i].first >= 0 && tek.second + d[i].second >= 0 && tek.first + d[i].first < 8 && tek.second + d[i].second < 8 && b[tek.first + d[i].first][tek.second + d[i].second] == 0){
				b[tek.first + d[i].first][tek.second + d[i].second] = b[tek.first][tek.second] + 1;
		        q.push(make_pair(tek.first + d[i].first, tek.second + d[i].second));
	        }
	}

	/*
	for (i = 0; i < 8; i++) {
		for (j = 0; j < 8; j++)
			cout << a[i][j] << " ";
		cout << "\n";
	}

	cout << "\n";
	for (i = 0; i < 8; i++) {
		for (j = 0; j < 8; j++)
			cout << b[i][j] << " ";
		cout << "\n";
	}
	*/

	for (i = 0; i < 8; i++)
		for (j = 0; j < 8; j++)
			if (abs(a[i][j] - b[i][j])%2==0 && min(a[i][j],b[i][j]) > 0 && max(a[i][j], b[i][j]) < mn)
				mn = max(a[i][j], b[i][j]);
	if (mn == 100)
		mn = 0;
	cout << mn - 1;
	return 0;
}