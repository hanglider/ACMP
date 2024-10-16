#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
using namespace std;
string st;
int i, j, k, t[1000][1000], prov[1000][1000][4], x, y, min_x, min_y, max_x, max_y, r_x, r_y;
pair <int, int> s, f, tek, d[4];
queue <pair<int, int>> point;
int main() {

	for (i = 0; i < 1000; i++)
		for (j = 0; j < 1000; j++)
			for (k = 0; k < 4; k++)
				prov[i][j][k] = -1;
	
	getline(cin, st);
	for (auto c : st) {
		switch (c) {
		case 'N':
			y--;
			break;
		case 'S':
			y++;
			break;
		case 'W':
			x--;
			break;
		case 'E':
			x++;
			break;
		}
		if (x < min_x)
			min_x = x;
		if (x > max_x)
			max_x = x;
		if (y < min_y)
			min_y = y;
		if (y > max_y)
			max_y = y;
	}
	if (min_y < 0)
		r_y = abs(min_y);
	if (min_x < 0)
		r_x = abs(min_x);

	min_x = min_y = 0;
	max_x += r_x;
	max_y += r_y;

	f.first = y + r_y;
	f.second = x + r_x;
	s.first = r_y;
	s.second = r_x;
	int yy = s.first;
	int xx = s.second;

	for (auto c : st) {
		switch (c) {
		case 'N':
			prov[yy][xx][0] = 0;
			yy--;
			prov[yy][xx][2] = 0;
			break;
		case 'S':
			prov[yy][xx][2] = 0;
			yy++;
			prov[yy][xx][0] = 0;
			break;
		case 'W':
			prov[yy][xx][3] = 0;
			xx--;
			prov[yy][xx][1] = 0;
			break;
		case 'E':
			prov[yy][xx][1] = 0;
			xx++;
			prov[yy][xx][3] = 0;
			break;
		}

	}

	d[1] = make_pair(0, 1); //E
	d[2] = make_pair(1, 0); //S
	d[3] = make_pair(0, -1);//W
	d[0] = make_pair(-1, 0);//N

	t[s.first][s.second] = 1;
	point.push(s);
	while (point.size()>0 && t[f.first][f.second] == 0) {
		tek = point.front();
		point.pop();		
		for (i = 0; i < 4; i++)
			if (tek.first + d[i].first <= max_y && tek.second + d[i].second <= max_x && t[tek.first + d[i].first][tek.second + d[i].second] == 0 && prov[tek.first + d[i].first][tek.second + d[i].second][(i+2)%4] == 0 && prov[tek.first][tek.second][i] == 0) {
				t[tek.first + d[i].first][tek.second + d[i].second] = t[tek.first][tek.second] + 1;
				point.push(make_pair(tek.first + d[i].first, tek.second + d[i].second));
			}
	}
	tek = f;
	st = "";
	while (tek != s) {
		for (i = 0; i < 4; i++)
			if (prov[tek.first + d[i].first][tek.second + d[i].second][(i+2)%4]==0 && t[tek.first + d[i].first][tek.second + d[i].second] == t[tek.first][tek.second] - 1) {
				switch (i) {
				case 0:
					st += 'N';
					break;
				case 3:
					st += 'W';
					break;
				case 2:
					st += 'S';
					break;
				case 1:
					st += 'E';
					break;
				}
				tek.first += d[i].first;
				tek.second += d[i].second;
				break;
			}
	}

	cout << st;
	return 0;
}