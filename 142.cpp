#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
int n, m, i, j, s, f, rast,ans, kol, last,fl;
vector<vector<int>> mn;
vector<pair<int, pair<int, int>>> reb;
int main() {
	cin >> n >> m;
	for (i = 0; i < m; i++) {
		cin >> s >> f >> rast;
		reb.push_back(make_pair(rast, make_pair(s,f)));
	}
	sort(reb.begin(), reb.end());
	for (auto r : reb) {
		s = r.second.first;
		f = r.second.second;
		int num=-1;
		fl = 0;
		for (i = 0; i < mn.size(); i++) {
			kol = 0;
			for (j = 0; j < mn[i].size(); j++)
				if (s == mn[i][j]) {
					kol++;
					last = s;
				}
				else if (f == mn[i][j]) {
					kol++;
					last = f;
				}
			if (kol == 2)
				break;
			if (kol==1){
				if (num==-1)
				 num = i;
				else {
					mn[num].insert(mn[num].end(), mn[i].begin(), mn[i].end());
					auto iter = mn.cbegin();
					mn.erase(iter + i);
					ans += r.first;
					fl = 1;
					break;
				}
			}
		}
		if (fl==0 && i == mn.size()) {
			if (num == -1) {
				vector<int> test;
				test.clear();
				test.push_back(s);
				test.push_back(f);
				mn.push_back(test);
			}
			else {
				if (last == s)
					mn[num].push_back(f);
				else mn[num].push_back(s);
			}
			ans += r.first;
		}
	}
	cout<<ans;
	return 0;
}