#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int s1, s2, s3;
    int maxIndex = 0, maxNum = 0;
    cin >> s1 >> s2 >> s3;
    vector<int> arr((s1+s2+s3+1), 0);

    for (int i = 1; i<s1+1; i++){
        for (int j = 1; j<s2+1; j++){
            for (int k = 1; k<s3+1; k++){
                arr[i+j+k] += 1;
            }
        }
    }

    for (int i = 3; i<(s1+s2+s3+1); i++){
        if (maxNum < arr[i]){
            maxIndex = i;
            maxNum = arr[i];
        }
    }

    cout << maxIndex;

    return 0;
}