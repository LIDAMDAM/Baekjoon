#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string str;
    cin >> str;
    vector<int> arr(26, 0);
    for (int i = 0; i<str.length(); i++){
        arr[str[i]-'a'] += 1;
    }
    
    for (int i = 0; i<26; i++){
        cout << arr[i] << ' ';
    }

    return 0;
}