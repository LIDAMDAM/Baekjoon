#include <iostream>
#include <string>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int testcasenum = 0;
	int ripit = 0;
	string str;

	cin >> testcasenum;
	for (int i = 0; i < testcasenum; i++) {
		cin >> ripit >> str;
		for (int j = 0; j < str.length(); j++) {
			for (int k = 0; k < ripit; k++) {
				cout << str[j];
			}
		}
		cout << "\n";
	}

	return 0;
}