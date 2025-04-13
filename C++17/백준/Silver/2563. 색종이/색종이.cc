#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int arr[100][100] = {0};
    int n = 0;
    int x = 0, y = 0;
    int count = 0;

    cin >> n;
    for (int i = 0; i<n; i++){
        cin >> x >> y;
        for (int j = 0; j<10; j++){
            for (int k = 0; k<10; k++)
                arr[x+j][y+k] = 1;
        }
    }

    for (int i = 0; i<100; i++){
        for (int j = 0; j<100; j++){
            if (arr[i][j] == 1){
                count += 1;
            }
        }
    }

    cout << count;

    return 0;
}