#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n = 0, m = 0;
	cin >> n >> m;
	vector<int> arr(n, 0);
	int i = 0, j = 0;

	for (int x = 0; x < n; x++)
		arr[x] = x + 1;

	for (int x = 0; x < m; x++) {
		cin >> i >> j;
		reverse(arr.begin() + (i - 1), arr.begin() + j);
	}

	for (int x = 0; x < n; x++) {
		cout << arr[x];
		if (n != x - 1)
			cout << " ";
	}
	cout << "\n";

	return 0;
}