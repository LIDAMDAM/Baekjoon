#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int a = 0, b = 0;

	while (cin >> a >> b)
		cout << a + b << "\n";

	return 0;
}