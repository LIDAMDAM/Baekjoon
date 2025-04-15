#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int total = 0;
    int tmp = 0;
    for (int i = 0; i<5; i++){
        cin >> tmp;
        total += tmp;
    }

    cout << total;

    return 0;
}