#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n = 0;
    int fibonacci1 = 1, fibonacci2 = 0;
    int ans = 0;
    cin >> n;

    if (n == 0){
        ans = 0;
    }
    else if (n == 1){
        ans = 1;
    }
    else {
        for (int i = 1; i<n; i++){
            ans = fibonacci1 + fibonacci2;
            fibonacci2 = fibonacci1;
            fibonacci1 = ans;
        }
    }

    cout << ans;

    return 0;
}