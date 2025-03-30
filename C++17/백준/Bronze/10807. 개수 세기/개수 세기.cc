#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n = 0;
	cin >> n;

	vector<int> arr(n);
	for (int i = 0; n > i; i++)
		cin >> arr[i];

	int v = 0, count = 0;
	cin >> v;
	for (int i = 0; n > i; i++)
		if (arr[i] == v)
			count++;

	cout << count;

	return 0;
}