#include <iostream>
#include <vector>
#include <string>
using namespace std;


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<int> original_pice = {1, 1, 2, 2, 2, 8};

    for (int i = 0; i<6; i++){
        int num = 0;
        cin >> num;
        cout << original_pice[i] - num;
        cout << " ";
    }

    return 0;
}