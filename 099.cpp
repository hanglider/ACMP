#include <iostream>
#include <queue>
using namespace std;

int i, j, k, h, m, n, ans[50][50][50];
char c[50][50][50];
pair <int, int> d[4];
pair<int, pair<int, int>> s, f, tek;
queue<pair<int, pair<int, int>>> q;

int main() {
	d[0] = make_pair(1, 0);
	d[1] = make_pair(-1, 0);
	d[2] = make_pair(0, 1);
	d[3] = make_pair(0, -1);

	cin >> h >> m >> n;
	for (i = 0; i < h; i++)
		for (j = 0; j < m; j++)
			for (k = 0; k < n; k++) {
				cin >> c[i][j][k];
				if (c[i][j][k] == '1') {
					s = make_pair(i, make_pair(j, k));
					ans[i][j][k] = 1;
				}
				else if (c[i][j][k] == '2') {
					f = make_pair(i, make_pair(j, k));
				}
			}
	q.push(s);

	while (q.size() > 0) {
		tek = q.front();
		q.pop();
		for (i=0;i<4;i++)
			if (tek.second.first + d[i].first >= 0 && tek.second.first + d[i].first < m && tek.second.second + d[i].second >= 0 && tek.second.second + d[i].second < n && ans[tek.first][tek.second.first + d[i].first][tek.second.second + d[i].second] == 0 && c[tek.first][tek.second.first + d[i].first][tek.second.second + d[i].second] != 'o') {
				ans[tek.first][tek.second.first + d[i].first][tek.second.second + d[i].second] = ans[tek.first][tek.second.first][tek.second.second] + 1;
				q.push(make_pair(tek.first, make_pair(tek.second.first + d[i].first, tek.second.second + d[i].second)));
			}
		if (tek.first + 1 < h && ans[tek.first + 1][tek.second.first][tek.second.second] == 0 && c[tek.first + 1][tek.second.first][tek.second.second] != 'o') {
			ans[tek.first+1][tek.second.first][tek.second.second] = ans[tek.first][tek.second.first][tek.second.second] + 1;
			q.push(make_pair(tek.first+1, make_pair(tek.second.first, tek.second.second)));
		}
	}

	cout << (ans[f.first][f.second.first][f.second.second]-1)*5;
	return 0;
}