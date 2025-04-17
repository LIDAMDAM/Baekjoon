#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<int> arr(3,0);
    for (int i = 0; i<3; i++){
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());
    cout << arr[1];

    return 0;
}