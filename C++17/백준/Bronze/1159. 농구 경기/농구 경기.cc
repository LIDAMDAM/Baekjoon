#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n = 0;
    string tmp = "0";
    vector<int> arr(26);
    int giveUp = 0;
    cin >> n;

    for (int i = 0; i<n; i++){
        cin >> tmp;
        arr[tmp[0]-'a'] += 1;
    }

    for (int i = 0; i<26; i++){
        if(arr[i]>4){
            cout << char(i+'a');
            giveUp = 1;
        }
    }

    if (giveUp == 0){
        cout << "PREDAJA";
    }

    return 0;
}