#include <iostream>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int num = 0;
    cin >> num;
    for (int i=1; i < num+1; i++){
        for (int j=0; j<num-i; j++){
            cout << " ";
        }
        for (int j=0; j<2*i-1; j++){
            cout << "*";
        }
        cout << "\n";
    }
    for (int i=1; i < num; i++){
        for (int j=0; j<i; j++){
            cout << " ";
        }
        for (int j=0; j< 2*num-2*i-1; j++){
            cout << "*";
        }
        cout <<"\n";
    }


    return 0;
}