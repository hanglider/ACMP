#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>
#include <stack>
#include <string>
#include <algorithm>
using namespace std;
char c;
string s;
int main()
{
	fstream fin("input.txt");
	while (getline(fin, s)) {
		stack <char> st;
			for (auto c : s) {
				if (c == '(' || c == '[' || c == '{')
					st.push(c);
				else if (c == ')' || c == ']' || c == '}'){
					if (st.size() > 0) {
						char cc = st.top();
						if ((c == ')' && cc == '(') || (c == ']' && cc == '[') || (c == '}' && cc == '{'))
							st.pop();
						else {
							st.push(c);
							break;
						}
					}
					else {
						st.push(c);
						break;
					}
				}
			}
			if (st.size() == 0)
				cout << 0;
			else cout << 1;
	}

	return 0;
}