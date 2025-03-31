#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	string s;
	cin >> s;
	vector<int> arr(26, -1);

	for (int i = 0; i < s.length(); i++) {
		if (arr[s[i] - 'a'] == -1)
			arr[s[i] - 'a'] = i;
	}

	for (int i = 0; i < 26; i++)
		cout << arr[i] << " ";

	cout << "\n";

	return 0;
}