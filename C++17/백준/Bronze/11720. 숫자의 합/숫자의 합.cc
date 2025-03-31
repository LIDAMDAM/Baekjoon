#include <iostream>
#include <string>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n = 0, total = 0;
	string s = "";
	cin >> n;
	cin >> s;

	for (int i = 0; i < n; i++) {
		total += s[i]-'0';
	}

	cout << total << "\n";

	return 0;
}