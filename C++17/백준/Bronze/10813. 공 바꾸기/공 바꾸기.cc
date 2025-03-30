#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n = 0, m = 0;
	cin >> n >> m;
	vector<int> arr(n, 0);
	int x = 0, y = 0;

	for (int i = 0; i < n; i++)
		arr[i] = i + 1;
	
	for (int i = 0; i < m; i++) {
		cin >> x >> y;
		swap(arr[x-1], arr[y-1]);
	}

	for (int i = 0; i < n; i++) {
		cout << arr[i];
		if (i != n - 1)
			cout << " ";
	}
	cout << "\n";

	return 0;
}