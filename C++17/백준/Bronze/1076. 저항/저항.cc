#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string alpha;
    vector<string> arr = {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};
    vector<int> numarr(3, 0);

    for (int i = 0; i<3; i++){
        cin >> alpha;
        for (int j = 0; j<10; j++){
            if(alpha == arr[j]){
                numarr[i] = j;
            }
        }
    }

    long long ans = (numarr[0] * 10 + numarr[1]) * (long long)pow(10, numarr[2]);
    cout << ans;

    return 0;
}