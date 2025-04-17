#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int score = 0;
    int total = 0;

    for (int i = 0; i<5; i++){
        cin >> score;
        if (score < 40){
            score = 40;
        }
        total += score;
    }

    cout << total/5;

    return 0;
}