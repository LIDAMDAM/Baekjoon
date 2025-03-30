#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n = 0, m = 0;
	cin >> n >> m;
	int i = 0, j = 0, k = 0;
	vector<int> arr(n, 0);
	
	for (int x = 0; x < m; x++) {
		cin >> i >> j >> k;
		for (int y = i-1; y < j; y++)
			arr[y] = k;
	}

	for (int x = 0; x < n; x++) {
		cout << arr[x];
		if (x != n - 1)
			cout << " ";
	}
	cout << "\n";

	return 0;
}