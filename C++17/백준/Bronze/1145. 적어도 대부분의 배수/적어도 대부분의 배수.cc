#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int count, ans = 0;
    vector<int> numArray(5);
    
    for (int i = 0; i<5; i++){
        cin >> numArray[i];
    }

    while(1){
        count = 0;
        ans += 1;
        for (int i = 0; i<5; i++){
            if(ans % numArray[i] == 0){
                count += 1;
            }
        }
        if (count >= 3){
            break;
        }
    }

    cout << ans;

    return 0;
}