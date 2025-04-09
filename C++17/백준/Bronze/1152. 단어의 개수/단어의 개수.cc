#include <iostream>
#include <string>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    int anser = 0;
    string str;
    while(cin >> str)
        anser++;
    
    cout << anser;

	return 0;
} 