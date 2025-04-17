#include <iostream>
#include <cmath>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t, a, b, tmp;
    cin >> t;
    for (int i = 0; i<t; i++){
        cin >> a >> b;
        tmp = 1;
        for (int j = 0; j<b; j++){
            tmp = tmp*a%10;
        }
        if (tmp == 0){
            tmp = 10;
        }
        cout << tmp << "\n";
    }

    return 0;
}