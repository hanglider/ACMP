#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;
string s, a, ss;
int i, j, n, k, poz[100000], p, jj, temp;
map<char, int> per;

void rec(int x) {
	string bff = "";
	if (x >= 0) {
		int tek = 0;
		int t = poz[x] + 1;
		if (s[t - 2] == 'D') {
			tek++;
			while (t < s.size() && s[t - 1] != ')' && tek == 1) {
				tek *= (int(s[t]) - int('0'));
				t += 2;
			}
		}
		else if (s[t - 2] == 'R') {
			while (t<s.size() && s[t] != ')' && tek == 0) {
				tek += (int(s[t]) - int('0'));
				t+=2;
			}
		}
		else if (s[t - 2] == 'T') tek = 1 - int(s[t]) + int('0');
		int xx = poz[x] - 1;
		int tmp = xx;
		while (s[tmp] != ')' && tmp < s.size())
			tmp++;
		while (s[xx] != ',' && s[xx] != '(' && xx > 0)
			xx--;

		if (xx > 0)
			bff = s.substr(0, xx + 1);

		s.erase(0, tmp + 1);
		s = bff + to_string(tek) + s;
		rec(x - 1);
	}
}

int main() {
	getline(cin, ss);
	cin >> n >> k;

	for (j = 0; j < ss.size(); j++)
		if (ss[j] == '(') {
			poz[p] = j;
			p++;
		}

	for (i = 0; i < n; i++) {
		s = ss;
		for (j = 0; j < k; j++) {
			cin >> a;
			if (a[2] == 'F')
				per[a[0]] = 0;
			else per[a[0]] = 1;
		}
		for (j = 0; j < s.size(); j++)
			if (per.find((s[j])) != per.end() && (s[j + 1] == ',' || s[j + 1] == ')')) {
				temp = per[s[j]];
				string buff = s.substr(0, j);
				s.erase(0, j + 1);
				s = buff + to_string(temp) + s;
			}

		rec(p - 1);
		per.clear();
		if (s == "0")
			cout << "FALSE" << endl;
		else cout << "TRUE" << endl;
	}
	return 0;
}