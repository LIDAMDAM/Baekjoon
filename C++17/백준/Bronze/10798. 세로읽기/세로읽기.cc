#include <iostream>
#include <string>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string arr [5];
    
    for (int i = 0; i<5; i++){
        cin >> arr[i];
    }

    for (int i = 0; i<15; i++){
        for (int j = 0; j<5; j++){
            if (i<arr[j].size()){
                cout << arr[j][i];
            }
        }
    }

    return 0;
}