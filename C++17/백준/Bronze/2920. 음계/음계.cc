#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<int> melody(8);
    int ascendPoint = 0, descendPoint = 0;

    for (int i = 0; i<8; i++){
        cin >> melody[i];
    }

    for (int i = 0; i<8; i++){
        if (melody[i] == i+1){
            ascendPoint++;
        }
        else if (melody[i] == 8-i){
            descendPoint++;
        }
    }

    if (ascendPoint == 8){
        cout << "ascending";
    }
    else if (descendPoint == 8){
        cout << "descending";
    }
    else {
        cout << "mixed";
    }

    return 0;
}