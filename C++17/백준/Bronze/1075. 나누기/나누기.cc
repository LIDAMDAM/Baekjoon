#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, f;
    cin >> n;
    cin >> f;
    int twoNum = n%100, tmp = n-twoNum;
    for (int i = 0; i< 100; i++){
        if ((tmp + i)%f == 0){
            tmp = i;
            break;
        }
    }

    if(tmp<10){
        cout << "0" << tmp;
    }
    else{
        cout << tmp;
    }

    return 0;
}