#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<vector<int>> arr(9, vector<int> (9));
    int maxx = 0, maxy = 0, maxnum = 0;

    for (int i = 0; i<9; i++){
        for (int j = 0; j<9; j++){
            cin >> arr[i][j];
        }
    }

    for (int i = 0; i<9; i++){
        for (int j = 0; j<9; j++){
            if (maxnum < arr[i][j]){
                maxnum = arr[i][j];
                maxx = i;
                maxy = j;
            }
        }
    }

    cout << maxnum << "\n" << maxx+1 << " " << maxy+1;

    return 0;
}