#include <iostream>
#include <queue>
#include <iomanip>
using namespace std;
int i, j, n, m, t[2000][2000],f;
char mp[2000][2000];
pair<int, int> s, r, tg, tek, d[4];
queue <pair<int, int>> q;
int main() {
	d[0] = make_pair(1, 0);
	d[1] = make_pair(0, 1);
	d[2] = make_pair(-1, 0);
	d[3] = make_pair(0, -1);
	cin >> n >> m;
	for (i = 0; i < n; i++)
		for (j = 0; j < m; j++) {
			cin >> mp[i][j];
			if (mp[i][j] == 'T')
				tg = make_pair(i, j);
			if (mp[i][j] == '.' && f == 0) {
				r = make_pair(i, j);
				f = 1;
			}
			if (mp[i][j]=='.')
				s = make_pair(i, j);
		}
	t[s.first][s.second] = 1;
	q.push(s);
	while (q.size() > 0) {
		tek = q.front();
		q.pop();
		for (i=0;i<4;i++)
			if (tek.first + d[i].first >= 0 && tek.first + d[i].first < n && tek.second + d[i].second >= 0 && tek.second + d[i].second < m) {
				if (mp[tek.first+d[i].first][tek.second + d[i].second] != '#' && t[tek.first + d[i].first][tek.second + d[i].second] == 0) {
					t[tek.first + d[i].first][tek.second + d[i].second] = t[tek.first][tek.second] + 1;
					q.push(make_pair(tek.first + d[i].first, tek.second + d[i].second));
				}
			}
	}

	/*
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++)
			cout << setw(4) << t[i][j] << setprecision(4) << " ";
		cout << "\n";
	}
	cout << t[r.first][r.second]<<"\n" << t[tg.first][tg.second] << "\n";
	*/
	cout << t[r.first][r.second]-1<<"\n";
	if (tg != s && t[tg.first][tg.second] == 0)
		cout << "Yes";
	else if (t[r.first][r.second] < t[tg.first][tg.second])
		cout << "Yes";
	else cout << "No";
	return 0;
}