#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    string grandma_num;
    vector<string> call_num = {"ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"};
    int time = 0;
    cin >> grandma_num;
    for (char c : grandma_num){
        for (int j = 0; j<8; j++){
            for (char d : call_num[j]){
                if (c == d) {
                    time += j+3;
                    break;
                }
            }
        }
    }

    cout << time;

    return 0;
} 