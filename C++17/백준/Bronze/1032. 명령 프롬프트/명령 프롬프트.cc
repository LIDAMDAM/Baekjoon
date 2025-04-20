#include <iostream>
#include <string>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int testCase = 0;
    string tmp1, tmp2;
    cin >> testCase;
    cin >> tmp1;
    if (testCase > 1){
        for (int i = 0; i<testCase; i++){
            cin >> tmp2;
            for (int j = 0; j<tmp1.length(); j++){
                if (tmp1[j] != tmp2[j]){
                    tmp1[j] = '?';
                }
            }
        }
    }
    cout << tmp1;

    return 0;
}