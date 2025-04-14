#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n = 0, m = 0;
    int tmp = 0;
    int maxNum = 0;
    cin >> n >> m;
    vector<int> arr;

    for (int i = 0; i<n; i++){
        cin >> tmp;
        arr.push_back(tmp);
    }

    for (int i = 0; i < n-2; i++){
        for (int j = i+1; j<n-1; j++){
            for (int k = j+1; k<n; k++){
                if ((arr[i]+arr[j]+arr[k] <= m) && (maxNum < arr[i]+arr[j]+arr[k])){
                    maxNum = arr[i]+arr[j]+arr[k];
                }
            }
        }
    }

    cout << maxNum;

    return 0;
}