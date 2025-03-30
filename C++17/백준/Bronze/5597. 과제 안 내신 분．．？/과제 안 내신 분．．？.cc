#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n = 0, count = 0;
	vector<int> arr(30, 0);

	for (int i = 0; i < 28; i++) {
		cin >> n;
		arr[n - 1] = 1;
	}

	for (int i = 0; i < 30; i++) {
		if (arr[i] == 0) {
			cout << i + 1 << "\n";
			count++;
		}

		if (count == 2)
			break;
	}

	return 0;
}